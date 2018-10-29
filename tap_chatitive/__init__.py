from tap_kit import TapExecutor, BaseClient, main_method


from .tags import TagsStream
from .campaigns import CampaignsStream
from .channels import ChannelsStream
from .transports import TransportsStream
from .subscribers import SubscribersStream


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
