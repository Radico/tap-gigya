from tap_kit import TapExecutor, BaseClient, main_method


from tap_chatitive.streams.tags import TagsStream
from tap_chatitive.streams.campaigns import CampaignsStream
from tap_chatitive.streams.channels import ChannelsStream
from tap_chatitive.streams.transports import TransportsStream
from tap_chatitive.streams.subscribers import SubscribersStream


STREAMS = [
    TagsStream,
    CampaignsStream,
    ChannelsStream,
    TransportsStream,
    SubscribersStream,
]

REQUIRED_CONFIG_KEYS = ["start_date", 'username', 'password']


class ChatitiveTap(TapExecutor):
    url = 'https://api.essential.to/v2/account/'
    pagination_type = 'next'
    auth_type = 'basic'


def main():
    main_method(
        REQUIRED_CONFIG_KEYS,
        ChatitiveTap,
        BaseClient,
        STREAMS
    )


if __name__ == '__main__':
    main()
