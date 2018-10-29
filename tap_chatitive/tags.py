from tap_kit.streams import Stream

class TagsStream(Stream):

    stream = 'tags'

    meta_fields = dict(
        key_properties=['sid'],
        replication_method='full',
        selected_by_default=False
    )

    schema = \
{
  "type": [
    "null",
    "object"
  ],
  "properties": {
    "name": {
      "type": [
        "null",
        "string"
      ]
    },
    "created_at": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    },
    "updated_at": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    },
    "account_sid": {
      "type": [
        "null",
        "string"
      ]
    },
    "canonical_name": {
      "type": [
        "null",
        "string"
      ]
    },
    "sid": {
      "type": [
        "null",
        "string"
      ]
    },
    "channel_sid": {
      "type": [
        "null",
        "string"
      ]
    },
    "deleted_at": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    }
  }
}
