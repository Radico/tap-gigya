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


REQUIRED_CONFIG_KEYS = ['secret', 'apiKey', 'UID', 'format']


class GigyaTap(TapExecutor):
    url = 'https://ids.eu1.gigya.com/'
    pagination_type = 'next'
    auth_type = 'basic_key'
    replication_key_format = 'timestamp'

    def build_params(self, stream, last_updated=0):
        query = "select  emails, data.subscriptions, UID, lastUpdatedTimestamp  from accounts where lastUpdatedTimestamp > {}".format(1537655907126)

        return {
            'query': query,
            'secret': stream.config['secret'],
            'apiKey': stream.config['apiKey'],
            'UID': stream.config['UID'],
            'format': stream.config['format'],
            'openCursor': True
        }

    def call_incremental_stream(self, stream):
        """
        Method to call all incremental synced streams
        """

        last_updated = format_last_updated_for_request(
            stream.update_and_return_bookmark(), self.replication_key_format)
        request_config = {
            'url': self.generate_api_url(stream),
            'headers': self.build_headers(),
            'params': self.build_params(stream, last_updated=last_updated),
            'run': True
        }

        print('hey')
        LOGGER.info("Extracting %s since %s" % (stream, last_updated))

        total_contacts_pulled = 0

        

        while request_config['run']:

            res = self.client.make_request(request_config)

            records = get_res_data(res.json(), self.get_res_json_key(stream))


            # transform_write_and_count(stream, records)

            total_contacts_pulled += res.json()['objectsCount']
            total_count = res.json()['totalCount']

            request_config = self.update_for_next_call(
                res,
                request_config,
                last_updated=last_updated
            )

            LOGGER.info("Pulled %s objects out of %s" % (total_contacts_pulled, total_count))

        return last_updated

    def update_for_next_call(self, res, request_config, last_updated=None):

        if 'nextCursorId' not in res.json():
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
