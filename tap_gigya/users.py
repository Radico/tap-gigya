from .streams import Stream
import singer


class UsersStream(Stream):

    stream = 'ids.search'

    meta_fields = dict(
        key_properties=['id'],
        replication_method='incremental',
        replication_key='last_updated',
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
        "UID": {
          "type": [
            "null",
            "string"
            ]
            },
        "emails": {
          "type": [
            "null",
            "string"
            ]
            },    
      }
    }




