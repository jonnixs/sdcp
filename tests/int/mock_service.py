from datetime import datetime
import json
import socket
import uuid

import websockets
from websockets.asyncio.server import ServerConnection


class MockServiceV3:
    async def handler(self, sock: ServerConnection):
        async for message in sock:
            message_obj = json.loads(message)

            if "echo" in message_obj:
                await sock.send(message_obj["echo"])
            elif cmd := message_obj.get("Data").get("Cmd"):
                await sock.send(
                    json.dumps(getattr(self, f"_control_{cmd}")(message_obj))
                )

    async def run(self):
        async with websockets.serve(self.handler, "127.0.0.1", 3030) as server:
            await server.serve_forever()

    def _control(self, obj: dict) -> dict:
        return {
            "Id": obj["Id"],
            "Data": {
                "Cmd": obj["Data"]["Cmd"],
                "Data": {"Ack": 0},
                "RequestID": obj["Data"]["RequestID"],
                "MainboardID": obj["Data"]["MainboardID"],
                "TimeStamp": int(datetime.now().timestamp()),
            },
            "Topic": f"sdcp/response/{obj["Data"]["MainboardID"]}",
        }

    def _control_255(self, obj: dict) -> dict:
        return self._control(obj)

    def _control_0(self, obj: dict) -> dict:
        return self._control(obj)

    def _control_1(self, obj: dict) -> dict:
        return self._control(obj)

    def _control_128(self, obj: dict) -> dict:
        return self._control(obj)

    def _control_130(self, obj: dict) -> dict:
        return self._control(obj)

    def _control_131(self, obj: dict) -> dict:
        return self._control(obj)

    def _control_132(self, obj: dict) -> dict:
        return self._control(obj)

    def _control_133(self, obj: dict) -> dict:
        return self._control(obj)

    def _control_192(self, obj: dict) -> dict:
        return self._control(obj)

    def _control_258(self, obj: dict) -> dict:
        return {
            "Id": obj["Id"],
            "Data": {
                "Cmd": 258,
                "Data": {
                    "Ack": 0,
                    "FileList": [
                        {
                            "name": "/usb/xxx",
                            "usedSize": 123456,
                            "totalSize": 123456,
                            "storageType": 0,
                            "type": 0,
                        }
                    ],
                },
                "RequestID": obj["Data"]["RequestID"],
                "MainboardID": obj["Data"]["MainboardID"],
                "TimeStamp": int(datetime.now().timestamp()),
            },
            "Topic": f"sdcp/response/{obj["Data"]["MainboardID"]}",
        }

    def _control_259(self, obj: dict) -> dict:
        return {
            "Id": obj["Id"],
            "Data": {
                "Cmd": 259,
                "Data": {"Ack": 0, "ErrData": ["/failed/file"]},
                "RequestID": obj["Data"]["RequestID"],
                "MainboardID": obj["Data"]["MainboardID"],
                "TimeStamp": int(datetime.now().timestamp()),
            },
            "Topic": f"sdcp/response/{obj["Data"]["MainboardID"]}",
        }

    def _control_320(self, obj: dict) -> dict:
        return {
            "Id": obj["Id"],
            "Data": {
                "Cmd": 320,
                "Data": {"Ack": 0, "HistoryData": ["taskuuid"]},
                "RequestID": obj["Data"]["RequestID"],
                "MainboardID": obj["Data"]["MainboardID"],
                "TimeStamp": int(datetime.now().timestamp()),
            },
            "Topic": f"sdcp/response/{obj["Data"]["MainboardID"]}",
        }

    def _control_321(self, obj: dict) -> dict:
        return {
            "Id": obj["Id"],
            "Data": {
                "Cmd": 321,
                "Data": {
                    "Ack": 0,
                    "HistoryDetailList": [
                        {
                            "Thumbnail": "xxx",
                            "TaskName": "xxx",
                            "BeginTime": int(datetime.now().timestamp()) - 300,
                            "EndTime": int(datetime.now().timestamp()),
                            "TaskStatus": 1,
                            "SliceInformation": {},
                            "AlreadyPrintLayer": 2,
                            "TaskId": "",
                            "MD5": "",
                            "CurrentLayerTalVolume": 0.02,
                            "TimeLapseVideoStatus": 0,
                            "TimeLapseVideoUrl": "xxxx",
                            "ErrorStatusReason": 0,
                        }
                    ],
                },
                "RequestID": obj["Data"]["RequestID"],
                "MainboardID": obj["Data"]["MainboardID"],
                "TimeStamp": int(datetime.now().timestamp()),
            },
            "Topic": f"sdcp/response/{obj["Data"]["MainboardID"]}",
        }

    def _control_386(self, obj: dict) -> dict:
        return {
            "Id": obj["Id"],
            "Data": {
                "Cmd": 321,
                "Data": {"Ack": 0, "VideoUrl": "url"},
                "RequestID": obj["Data"]["RequestID"],
                "MainboardID": obj["Data"]["MainboardID"],
                "TimeStamp": int(datetime.now().timestamp()),
            },
            "Topic": f"sdcp/response/{obj["Data"]["MainboardID"]}",
        }

    def _control_387(self, obj: dict) -> dict:
        return self._control(obj)
