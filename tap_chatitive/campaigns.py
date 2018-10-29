from tap_kit.streams import Stream

class CampaignsStream(Stream):

    stream = 'campaigns'

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
    "body": {
      "type": [
        "null",
        "string"
      ]
    },
    "exclude_numbers": {
      "type": [
        "null"
      ]
    },
    "channel_sid": {
      "type": [
        "null",
        "string"
      ]
    },
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
    "shorten_urls": {
      "type": [
        "null",
        "boolean"
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
    "include_numbers": {
      "items": {
        "type": [
          "null",
          "string"
        ]
      },
      "type": [
        "null",
        "array"
      ]
    },
    "send_at": {
      "type": [
        "null",
        "string"
      ]
    },
    "sid": {
      "type": [
        "null",
        "string"
      ],
      "format": "date-time"
    },
    "results": {
      "items": {
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
          "success": {
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
          "failure": {
            "type": [
              "null",
              "integer"
            ]
          },
          "owner_sid": {
            "type": [
              "null",
              "string"
            ]
          },
          "file": {
            "type": [
              "null",
              "object"
            ],
            "properties": {
              "url": {
                "type": [
                  "null"
                ]
              }
            }
          },
          "sid": {
            "type": [
              "null",
              "string"
            ]
          },
          "report": {
            "type": [
              "null"
            ]
          },
          "owner_type": {
            "type": [
              "null",
              "string"
            ]
          },
          "pending": {
            "type": [
              "null",
              "integer"
            ]
          }
        }
      },
      "type": [
        "null",
        "array"
      ]
    },
    "media_urls": {
      "type": [
        "null"
      ]
    },
    "send_to_inboxed": {
      "type": [
        "null",
        "boolean"
      ]
    },
    "external_ref_id": {
      "type": [
        "null",
        "string"
      ]
    },
    "tag_expression": {
      "type": [
        "null",
        "object"
      ],
      "properties": {
        "operator": {
          "type": [
            "null",
            "string"
          ]
        },
        "right": {
          "type": [
            "null"
          ]
        },
        "tag_sids": {
          "items": {
            "type": [
              "null",
              "string"
            ]
          },
          "type": [
            "null",
            "array"
          ]
        },
        "left": {
          "type": [
            "null"
          ]
        }
      }
    }
  }
}
