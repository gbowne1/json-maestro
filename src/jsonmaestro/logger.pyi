from typing import Any, NoReturn


def log(message: str, **kwargs: Any) -> None:
    ...


def logf(format_str: str, *args: Any) -> None:
    ...


def debug(message: str, **kwargs: Any) -> None:
    ...


def debugf(format_str: str, *args: Any) -> None:
    ...


def info(message: str, **kwargs: Any) -> None:
    ...


def infof(format_str: str, *args: Any) -> None:
    ...


def warn(message: str, **kwargs: Any) -> None:
    ...


def warnf(format_str: str, *args: Any) -> None:
    ...


def error(message: str, **kwargs: Any) -> None:
    ...


def errorf(format_str: str, *args: Any) -> None:
    ...


def fatal(message: str, **kwargs: Any) -> NoReturn:
    ...


def fatalf(format_str: str, *args: Any) -> NoReturn:
    ...
