import pytest

from sdcp.discovery import Service


class TestV3:
    @pytest.mark.asyncio
    async def test_discovery_not_found(self):
        result = await Service().broadcast()

        assert result == []

    @pytest.mark.asyncio
    async def test_quick_discovery(self, fixture_mock_device_1, fixture_mock_device_2):
        result = await Service().broadcast(fast=True)

        assert len(result) == 1
        assert result[0].model in ["Mars", "Saturn 4 Ultra"]
        assert str(result[0].addr) in ["127.0.0.1", "127.0.0.2"]

    @pytest.mark.asyncio
    async def test_discovery(self, fixture_mock_device_1, fixture_mock_device_2):
        result = await Service().broadcast()

        s_result = sorted(result, key=lambda x: x.id)

        assert len(s_result) == 2
        assert s_result[0].model == "Saturn 4 Ultra"
        assert str(s_result[0].addr) == "127.0.0.1"

        assert result[1].model == "Mars"
        assert str(result[1].addr) == "127.0.0.2"
