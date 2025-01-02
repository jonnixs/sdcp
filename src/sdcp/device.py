"""Docs here."""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime
import ipaddress
from typing import Any, Self

from websockets.asyncio.client import ClientConnection, connect


class Device:
    """Something."""

    @classmethod
    def create(cls, data: dict[str, Any]) -> Self:
        protocol = data["Data"]["ProtocolVersion"]

        if protocol == "V3.0.0":
            return cls(**_parse_v3(data))
        raise NotImplementedError("Protocol version not supported.")

    def __init__(
        self,
        id: str,
        addr: ipaddress.IPv4Address | str,
        name: str,
        make: str,
        make_id: str,
        model: str,
        protocol: str,
        firmware: str,
    ):
        """Docs here."""
        self._conn: ClientConnection
        self._port = 3030
        self._path = "/websocket"
        self._requests: dict[str, tuple[Callable, int]] = {}

        self.id = id
        self.name = name
        self.make = make
        self.make_id = make_id
        self.model = model
        self.addr = addr
        self.protocol = protocol
        self.firmware = firmware

    def __repr__(self):
        module = type(self).__module__
        qualname = type(self).__qualname__
        return f"<{module}.{qualname} object at {hex(id(self))} with ID '{self.id}' and IP '{self.addr}'>"

    async def connect(self) -> None:
        """Docs here."""
        self._conn = await connect(f"{self.addr}:{self._port}{self._path}")

    async def send(
        self, data: str, /, callback: tuple[str, Callable] | None = None
    ) -> bool:
        """Docs here."""
        try:
            await self._conn.send(data)

            # Send successful
            if callback:
                self._requests[callback[0]] = (
                    callback[1],
                    int(datetime.now().timestamp()),
                )
        except Exception:
            return False

        return True

    async def recv(self) -> Any:  # Topic:
        """Docs here."""
        message = await self._conn.recv()

        return message


def _parse_v3(data: dict) -> dict[str, str]:
    args = {
        "id": str(data["Data"]["MainboardID"]),
        "name": str(data["Data"]["Name"]),
        "make": str(data["Data"]["BrandName"]),
        "make_id": str(data["Id"]),
        "model": str(data["Data"]["MachineName"]),
        "addr": str(data["Data"]["MainboardIP"]),
        "protocol": str(data["Data"]["ProtocolVersion"]),
        "firmware": str(data["Data"]["FirmwareVersion"]),
    }

    return args
