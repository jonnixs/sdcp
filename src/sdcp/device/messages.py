from __future__ import annotations
from abc import ABC, abstractmethod

from sdcp.consts import SDCP_MACHINE_STATUS, SDCP_PRINT_ERROR

from . import Device


def factory(message: dict) -> Message:
    topic: str = message["Topic"]
    topic_type = topic.split("/")[1]

    if topic_type == "response":
        # Requested
        class_ = command_response_map[message["Data"]["Cmd"]]
        return class_(message)
    elif topic_type == "status":
        return Status(message)
    elif topic_type == "attributes":
        return Attributes(message)
    elif topic_type == "error":
        return Error(message)
    elif topic_type == "notice":
        return Notice(message)
    else:
        raise Exception


class Message(ABC):
    def __init__(self, message: dict):
        self._message = message

    @abstractmethod
    def update(self, device: Device) -> None:
        raise NotImplementedError


class Status(Message):
    def update(self, device: Device) -> None:
        status_data = self._message["Status"]

        device.current_status = (
            status_data["CurrentStatus"],
            SDCP_MACHINE_STATUS[status_data["CurrentStatus"]],
        )
        device.previous_status = (
            status_data["PreviousStatus"],
            SDCP_MACHINE_STATUS[status_data["PreviousStatus"]],
        )
        device.print_screen = status_data["PrintScreen"]
        device.release_film = status_data["ReleaseFilm"]
        device.temp_of_uv_led = status_data["TempOfUVLED"]
        device.time_lapse_status = not status_data["TimeLapseStatus"]
        device.temp_of_box = status_data["TempOfBox"]
        device.target_temp_of_box = status_data["TempTargetBox"]
        device.print_info.status = (
            status_data["PrintInfo"]["Status"],
            SDCP_MACHINE_STATUS[status_data["PrintInfo"]["Status"]],
        )
        device.print_info.current_layer = status_data["PrintInfo"]["CurrentLayer"]
        device.print_info.total_layers = status_data["PrintInfo"]["TotalLayer"]
        device.print_info.current_ticks = status_data["PrintInfo"]["CurrentTicks"]
        device.print_info.total_ticks = status_data["PrintInfo"]["TotalTicks"]
        device.print_info.file_name = status_data["PrintInfo"]["Filename"]
        device.print_info.error = (
            status_data["PrintInfo"]["ErrorNumber"],
            SDCP_PRINT_ERROR[status_data["PrintInfo"]["ErrorNumber"]],
        )
        device.print_info.task_id = status_data["PrintInfo"]["TaskId"]


class Attributes(Message):
    """Unsupported at present."""

    def update(self, device: Device) -> None: ...


class Error(Message):
    """Unsupported at present."""

    def update(self, device: Device) -> None: ...


class Notice(Message):
    """Unsupported at present."""

    def update(self, device: Device) -> None: ...


class Response(Message):
    def update(self, device: Device) -> None:
        return


class CommandResponse0(Response): ...


class CommandResponse1(Response): ...


class CommandResponse128(Response): ...


class CommandResponse129(Response): ...


class CommandResponse130(Response): ...


class CommandResponse131(Response): ...


class CommandResponse132(Response): ...


class CommandResponse133(Response): ...


class CommandResponse192(Response): ...


class CommandResponse255(Response): ...


class CommandResponse258(Response): ...


class CommandResponse259(Response): ...


class CommandResponse320(Response): ...


class CommandResponse321(Response): ...


class CommandResponse386(Response): ...


class CommandResponse387(Response): ...


command_response_map = {
    0: CommandResponse0,
    1: CommandResponse1,
    128: CommandResponse128,
    129: CommandResponse129,
    130: CommandResponse130,
    131: CommandResponse131,
    132: CommandResponse132,
    133: CommandResponse133,
    192: CommandResponse192,
    255: CommandResponse255,
    258: CommandResponse258,
    259: CommandResponse259,
    320: CommandResponse320,
    321: CommandResponse321,
    386: CommandResponse386,
    387: CommandResponse387,
}
