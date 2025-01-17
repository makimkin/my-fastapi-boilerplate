# endregion-------------------------------------------------------------------------
# region PRODUCER CONTAINER
# ----------------------------------------------------------------------------------
from aiokafka import AIOKafkaProducer
from dishka import provide, Scope

from settings.config import Config


class KafkaProducerContainer:
    @provide(scope=Scope.APP)
    def get_kafka_producer(self, config: Config) -> AIOKafkaProducer:
        return AIOKafkaProducer(bootstrap_servers=config.KAFKA_URI)


# endregion-------------------------------------------------------------------------
