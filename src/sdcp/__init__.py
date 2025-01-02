"""Package doc."""

from typing import Any

from .config import Config
from .device import Device
from .discovery import Service as DiscoveryService


class SDCP:
    """Some comment here."""

    def __init__(self, config: Config | dict[str, Any] = {}):
        """Init comments here."""
        self._config = config if isinstance(config, Config) else Config(config)
        self._discovery: DiscoveryService | None = None

    @property
    def discover(self) -> DiscoveryService:
        """Some comment here."""
        if self._discovery is None:
            self._discovery = DiscoveryService(self._config)

        return self._discovery


__all__ = ["Config", "SDCP", "Device"]
