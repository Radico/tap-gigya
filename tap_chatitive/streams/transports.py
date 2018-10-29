from tap_kit.streams import Stream

class TransportsStream(Stream):

    stream = 'transports'

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
    "status": {
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
    "protocol": {
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
    "status_updated_at": {
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
    "endpoint": {
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
    }
  }
}
