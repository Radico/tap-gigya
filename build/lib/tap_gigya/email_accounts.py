from .streams import Stream
import singer


class EmailAccountsStream(Stream):

    stream = 'email_accounts'

    meta_fields = dict(
        key_properties=['id'],
        replication_method='incremental',
        replication_key='last_updated',
        incremental_search_key='updated_after',
        selected_by_default=False
    )

    schema = \
    {
      "properties": {
      }
    }

    def get_query_url(self, last_updated):
        return "select email,\n subscriptions,\n data,\n UID,\n lastUpdatedTimestamp,\n profile.profileURL,\n profile.lastName,\n profile.gender,\n profile.locale,\n profile.email,\n profile.firstName from emailAccounts\n where lastUpdatedTimestamp > {} order by lastUpdatedTimestamp \nlimit 10000".format(last_updated)




