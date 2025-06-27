from typing import Any
from controller import RegisterController


MAPPING = {
    "register": RegisterController,
}


def controller(command: str, data: Any = None):
    MAPPING[command](data)
