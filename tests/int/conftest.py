import pytest
import threading

from .mock_device import MockDevice


@pytest.fixture(scope="function")
def fixture_mock_device_1():
    with MockDevice() as device:
        thread = threading.Thread(target=device.run)
        thread.daemon = True
        thread.start()

        yield device


@pytest.fixture(scope="function")
def fixture_mock_device_2():
    with MockDevice(machine_name="Mars", mainboard_ip="127.0.0.2") as device:
        thread = threading.Thread(target=device.run)
        thread.daemon = True
        thread.start()

        yield device
