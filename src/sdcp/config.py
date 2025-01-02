"""Docs here."""

from typing import Any


class Config:
    """Some comment here."""

    def __init__(self, values: dict[str, Any]):
        """Docs here."""
        self.discovery_timeout: tuple[int, int] = values.get(
            "discovery_timeout",
            (
                5,
                1,
            ),
        )
