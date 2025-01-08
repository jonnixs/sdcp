"""Docs here."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
import ipaddress
from typing import Any, Self


@dataclass
class PrintInfo:
    status: tuple[int, str] | None = None
    current_layer: int | None = None
    total_layers: int | None = None
    current_ticks: int | None = None
    total_ticks: int | None = None
    file_name: str | None = None
    error: tuple[int, str] | None = None
    task_id: str | None = None


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
        self._port = 3030
        self._path = "/websocket"
        self._requests: dict[str, tuple[Callable, int]] = {}

        # Discovery
        self.id = id
        self.name = name
        self.make = make
        self.make_id = make_id
        self.model = model
        self.addr = addr
        self.protocol = protocol
        self.firmware = firmware

        # Device Status
        self.current_status: tuple[int, str] | None = None
        self.previous_status: tuple[int, str] | None = None
        self.print_screen: int | None = None
        self.release_film: int | None = None
        self.temp_of_uv_led: int | None = None
        self.time_lapse_status: bool | None = None
        self.temp_of_box: int | None = None
        self.target_temp_of_box: int | None = None
        self.print_info = PrintInfo()

    def __repr__(self):
        module = type(self).__module__
        qualname = type(self).__qualname__
        return f"<{module}.{qualname} object at {hex(id(self))} with ID '{self.id}' and IP '{self.addr}'>"

    @property
    def port(self):
        return self._port

    @property
    def path(self):
        return self._path


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
