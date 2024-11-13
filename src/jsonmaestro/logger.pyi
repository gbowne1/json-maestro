from typing import Any

NO_LEVEL: int
DEBUG_LEVEL: int
INFO_LEVEL: int
WARN_LEVEL: int
ERROR_LEVEL: int
FATAL_LEVEL: int

RESET_COLOR: str
DEBUG_COLOR: str
INFO_COLOR: str
WARN_COLOR: str
ERROR_COLOR: str
FATAL_COLOR: str


# Functions
def logger_print(level: int, message: str) -> None:
	...


def construct_message(message: str, **kwargs: dict[Any, Any]) -> str:
	...


def log(message: str, **kwargs: dict[Any, Any]) -> None:
	...


def debug(message: str, **kwargs: dict[Any, Any]) -> None:
	...


def info(message: str, **kwargs: dict[Any, Any]) -> None:
	...


def warn(message: str, **kwargs: dict[Any, Any]) -> None:
	...


def error(message: str, **kwargs: dict[Any, Any]) -> None:
	...


def fatal(message: str, **kwargs: dict[Any, Any]) -> None:
	...
