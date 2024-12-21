# endregion-------------------------------------------------------------------------
# region MEMORY PRODUCER
# ----------------------------------------------------------------------------------
from dataclasses import dataclass, field
from collections import defaultdict

from .base import ProducerBase


@dataclass
class ProducerMemory(ProducerBase):
    events: dict[str, list[bytes]] = field(default_factory=lambda: defaultdict(list))

    async def send_message(self, topic: str, value: bytes) -> None:
        self.events[topic].append(value)

    async def close(self) -> None:
        await super().close()

    async def connect(self) -> None:
        await super().connect()


# endregion-------------------------------------------------------------------------
