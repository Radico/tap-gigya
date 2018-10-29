from tap_kit import TapExecutor, BaseClient, main_method


from .streams import STREAMS

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
