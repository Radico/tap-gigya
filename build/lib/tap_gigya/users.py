from .streams import Stream

class UsersStream(Stream):

    stream = 'ids.search'

    meta_fields = dict(
        key_properties=['id'],
        replication_method='incremental',
        replication_key='created_at',
        incremental_search_key='updated_after',
        selected_by_default=False
    )

    schema = \
    {
      "type": [
        "null",
        "object"
      ],
      "properties": {
      }
    }



