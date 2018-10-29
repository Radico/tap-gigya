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

if __name__ == '__main__':
    main()