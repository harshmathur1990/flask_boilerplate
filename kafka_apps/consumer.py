import logging
import simplejson as json
from config import KAFKAHOST, ZOOKEEPER, KAFKATOPIC

from flask_script import Manager
from pykafka import KafkaClient, common

logger = logging.getLogger(__name__)

KafkaConsumerCommand = Manager(usage="Consumer for order service publications")


@KafkaConsumerCommand.option('-g', '--group_ids', dest='group_no', default=1,
                                         help=("group no (must be different for different partitions)"))
def replay_test(group_no):
    try:
        client = KafkaClient(hosts=KAFKAHOST)
    except Exception as e:
        return
    group_id = KAFKATOPIC + u'{}'.format(group_no)
    try:
        topic = client.topics[KAFKATOPIC]
        balanced_consumer = topic.get_balanced_consumer(
            consumer_group=str(group_id),
            auto_commit_enable=True,
            reset_offset_on_start=True,
            auto_offset_reset=common.OffsetType.LATEST,
            use_rdkafka=False,
            zookeeper_connect=ZOOKEEPER
        )
        for message in balanced_consumer:
            if message is not None:
                message_dict = json.loads(message.value)
                # do whatever you want with data
                pass

    except Exception as e:
        logger.exception(e)
