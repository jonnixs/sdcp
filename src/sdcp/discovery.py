"""Module docs."""

from __future__ import annotations

import json
import logging
import socket
from typing import TYPE_CHECKING

from . import Device

if TYPE_CHECKING:
    from . import Config


_LOGGER = logging.getLogger(__name__)


class Service:
    """Service class."""

    def __init__(self, config: Config | None = None):
        """Initialize."""
        self.timeout, self.quick_timeout = (
            config.discovery_timeout
            if config is not None
            else (
                5,
                1,
            )
        )

    async def broadcast(self, address: str = "", /, fast=False) -> list[Device]:
        """Broadcast for device announcements."""
        # UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        # Set for broadcasting.
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Timeout after 2 seconds. Should be plenty of time for all devices
        # to respond to the broadcast.
        sock.settimeout(self.quick_timeout if fast else self.timeout)
        # Bind to any free available port.
        sock.bind((address, 0))

        # Use broadcast address to send M99999 on port 3000 per the docs.
        msg = b"M99999"
        sock.sendto(msg, ("255.255.255.255", 3000))

        devices = []
        while True:
            try:
                # Data is relatively restricted in broadcast results at time
                # of writing, so 512 bytes should be fine
                data, _ = sock.recvfrom(512)
                devices.append(await self._parse_message(data))

                if fast:
                    # Probably only wanting to confirm > 0 devices available
                    break
            except TimeoutError:
                # Properly close the socket file descriptor
                sock.close()
                break
        return devices

    async def _parse_message(self, message: bytes) -> Device:
        try:
            mess_obj = json.loads(message)
        except json.JSONDecodeError as err:
            # If the JSON cannot be decoded something went wrong or the
            # discovered device is not adhereing to SDCP. Ignore it.
            _LOGGER.error("Failed to parse discovery response as JSON.")
            raise Exception from err

        return Device.create(mess_obj)
