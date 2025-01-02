import json
import socket
import uuid


class MockDevice:
    def __init__(
        self,
        /,
        name="3D Printer",
        machine_name="Saturn 4 Ultra",
        brand_id="f25273b12b094c5a8b9513a30ca60049",
        brand_name="ELEGOO",
        mainboard_ip="127.0.0.1",
        mainboard_id=str(uuid.uuid4()),
        protocol_version="V3.0.0",
        firmware_version="V1.2.8",
    ):
        if protocol_version == "V3.0.0":
            self.message = json.dumps(
                {
                    "Id": brand_id,
                    "Data": {
                        "Name": name,
                        "MachineName": machine_name,
                        "BrandName": brand_name,
                        "MainboardIP": mainboard_ip,
                        "MainboardID": mainboard_id,
                        "ProtocolVersion": protocol_version,
                        "FirmwareVersion": firmware_version,
                    },
                }
            ).encode()
        else:
            raise NotImplementedError

        self._device_sock = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP
        )
        self._device_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        # Enable broadcasting mode
        self._device_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def __enter__(self):
        self._device_sock.bind(
            (
                "",
                3000,
            )
        )
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._device_sock.close()

    def run(self):
        try:
            while True:
                _, addr = self._device_sock.recvfrom(1024)
                self._device_sock.sendto(self.message, addr)
        except:
            ...
