from tap_kit.streams import Stream

class SubscribersStream(Stream):

    stream = 'subscribers'

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
    "phone_number": {
      "type": [
        "null",
        "string"
      ]
    },
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
    "sid": {
      "type": [
        "null",
        "string"
      ]
    },
    "cs_state_data": {
      "type": [
        "null"
      ]
    },
    "subscribed_at": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    },
    "created_at": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    },
    "external_user_id": {
      "type": [
        "null",
        "string"
      ]
    },
    "unsubscribed_at": {
      "type": [
        "null"
      ]
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
    "cs_provider_id": {
      "type": [
        "null"
      ]
    },
    "transport_sid": {
      "type": [
        "null",
        "string"
      ]
    },
    "carrier_updated_at": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    },
    "facebook_id": {
      "type": [
        "null"
      ]
    },
    "added_to_inbox_at": {
      "type": [
        "null"
      ],
      "format": "date-time"
    },
    "email_address": {
      "type": [
        "null",
        "string"
      ]
    },
    "carrier": {
      "type": [
        "null",
        "string"
      ]
    }
  }
}
