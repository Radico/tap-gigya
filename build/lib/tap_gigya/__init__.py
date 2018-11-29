from .client import BaseClient
from .utils import main_method
from .executor import TapExecutor
from .users import UsersStream

from .utils import (
    stream_is_selected, transform_write_and_count, safe_to_iso8601,
    format_last_updated_for_request, get_res_data
)

import sys
import json

import singer
import base64

from singer.catalog import Catalog, CatalogEntry, Schema

LOGGER = singer.get_logger()


STREAMS = [
    UsersStream,
]


REQUIRED_CONFIG_KEYS = ['api_secret', 'api_key', 'user_id']


class GigyaTap(TapExecutor):
    url = 'https://ids.eu1.gigya.com/'
    pagination_type = 'next'
    auth_type = 'basic_key'
    replication_key_format = 'timestamp'

    def build_params(self, stream, last_updated):
        query = "select  emails,\n data,\n UID,\n lastUpdatedTimestamp\n from accounts\n where lastUpdatedTimestamp > {} \nlimit 10000".format(last_updated)
        LOGGER.info('\nQuery running is:\n {}'.format(query))
        return {
            'query': query,
            'secret': stream.config['api_secret'],
            'apiKey': stream.config['api_key'],
            'UID': stream.config['user_id'],
            'format': 'json',
            'openCursor': True,
            'httpStatusCodes': True
        }

    def call_incremental_stream(self, stream):
        """
        Method to call all incremental synced streams
        """

        last_updated = stream.update_and_return_bookmark()

        
        request_config = {
            'url': self.generate_api_url(stream),
            'headers': self.build_headers(),
            'params': self.build_params(stream, last_updated=last_updated),
            'run': True
        }

        LOGGER.info("Extracting %s since %s" % (stream, last_updated))

        total_contacts_pulled = 0

        

        while request_config['run']:

            res = self.client.make_request(request_config)
            
            records = res.json()['results']

            transform_write_and_count(stream, records)

            total_contacts_pulled += res.json()['objectsCount']
            total_count = res.json()['totalCount']

            last_updated = self.get_max_last_updated(last_updated, records)

            request_config = self.update_for_next_call(
                res,
                request_config,
                last_updated=last_updated
            )

            LOGGER.info("Pulled %s objects out of %s" % (total_contacts_pulled, total_count))
        
        LOGGER.info('MAX UPDATED: {}'.format(last_updated))
        return str(last_updated)
    
    def get_max_last_updated(self, last_updated, records):
        for r in records:
            last_updated = max(int(last_updated), r['lastUpdatedTimestamp'])
        return last_updated

    def update_for_next_call(self, res, request_config, last_updated=None):

        if 'nextCursorId' not in res.json():
            LOGGER.info('Ending now, last response json is:')
            LOGGER.info(res.json())
            request_config['run'] = False
            return request_config

        nextCursorId = res.json()['nextCursorId']

        if 'query' in request_config['params']:
            del request_config['params']['query']
        
        if 'openCursor' in request_config['params']:
            del request_config['params']['openCursor']

        request_config['params']['cursorId'] = nextCursorId

        return request_config



def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        GigyaTap,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
