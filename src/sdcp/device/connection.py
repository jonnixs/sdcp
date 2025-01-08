from collections.abc import Callable
import logging
import json
from typing import Awaitable
from websockets.asyncio.client import ClientConnection, connect

from . import Device
from .messages import factory as message_factory


_LOGGER = logging.getLogger(__name__)


class Connection:
    def __init__(self, device: Device):
        self._conn: ClientConnection | None = None
        self._device = device
        self._tracking: dict[str, Callable] = {}

    async def connect(self) -> ClientConnection:
        self._conn = await connect(f"{self._device.addr}:{self._device.port}")

        return self._conn

    async def recv(self):
        if not self._conn:
            await self.connect()
            assert isinstance(self._conn, ClientConnection)

        while True:
            try:
                message = json.loads(await self._conn.recv())

                msg_obj = message_factory(message)
                msg_obj.update(self._device)
            except (ValueError, TypeError):
                _LOGGER.error(
                    "An error occured while receiving a websocket message from device %s; %s"
                    % (self._device.id, self._device.addr),
                    exc_info=True,
                )
                continue

    async def send(self, message: dict) -> Awaitable:
        if not self._conn:
            await self.connect()
            assert isinstance(self._conn, ClientConnection)

        return self._conn.send(message)
