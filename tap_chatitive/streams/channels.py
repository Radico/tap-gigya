from tap_kit.streams import Stream

class ChannelsStream(Stream):

    stream = 'channels'

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
    "min_campaign_delay_mins": {
      "type": [
        "null",
        "integer"
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
    "bot_sid": {
      "type": [
        "null",
        "string"
      ]
    },
    "onreceived_url": {
      "type": [
        "null"
      ]
    },
    "area_codes": {
      "type": [
        "null"
      ]
    },
    "sid": {
      "type": [
        "null",
        "string"
      ]
    },
    "received_paused_at": {
      "type": [
        "null"
      ],
      "format": "date-time"
    },
    "deliveries_paused_at": {
      "type": [
        "null"
      ],
      "format": "date-time"
    },
    "cs_provider_data": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "welcome_new_subscribers": {
          "type": [
            "null",
            "boolean"
          ]
        },
        "enabled": {
          "type": [
            "null",
            "boolean"
          ]
        },
        "enable_new_outbound_subscribers": {
          "type": [
            "null",
            "boolean"
          ]
        }
      }
    }
  }
}
