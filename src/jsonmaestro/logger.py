from typing import Any, NoReturn

try:
	from .helpers import can_use_match
except ImportError:  # for debugging
	from helpers import can_use_match

if can_use_match():
	try:
		from ._logger import logger_print as _logger_print
	except ImportError:  # for debugging
		from _logger import logger_print as _logger_print
else:
	try:
		from ._logger39 import logger_print as _logger_print
	except ImportError:  # for debugging
		from _logger39 import logger_print as _logger_print

try:
	from .constants import (
	    DEBUG_LEVEL,
	    ERROR_LEVEL,
	    FATAL_LEVEL,
	    INFO_LEVEL,
	    NO_LEVEL,
	    WARN_LEVEL,
	)
except ImportError:  # for debugging
	from constants import (
	    DEBUG_LEVEL,
	    ERROR_LEVEL,
	    FATAL_LEVEL,
	    INFO_LEVEL,
	    NO_LEVEL,
	    WARN_LEVEL,
	)


def _construct_message(message: str, **kwargs: Any) -> str:
	if kwargs:
		context_mesage = "".join(
		    f"\t{key}={value}\n"
		    for key, value in kwargs.items()).removesuffix("\n")
		return f"{message} |\n{context_mesage}"
	else:
		return message


def log(message: str, **kwargs: Any):
	_logger_print(NO_LEVEL, _construct_message(message, **kwargs))


def logf(format_str: str, *args: Any):
	_logger_print(NO_LEVEL, _construct_message(format_str.format(*args)))


def debug(message: str, **kwargs: Any):
	_logger_print(DEBUG_LEVEL, _construct_message(message, **kwargs))


def debugf(format_str: str, *args: Any):
	_logger_print(DEBUG_LEVEL, format_str.format(*args))


def info(message: str, **kwargs: Any):
	_logger_print(INFO_LEVEL, _construct_message(message, **kwargs))


def infof(format_str: str, *args: Any):
	_logger_print(INFO_LEVEL, format_str.format(*args))


def warn(message: str, **kwargs: Any):
	_logger_print(WARN_LEVEL, _construct_message(message, **kwargs))


def warnf(format_str: str, *args: Any):
	_logger_print(WARN_LEVEL, format_str.format(*args))


def error(message: str, **kwargs: Any):
	_logger_print(ERROR_LEVEL, _construct_message(message, **kwargs))


def errorf(format_str: str, *args: Any):
	_logger_print(ERROR_LEVEL, format_str.format(*args))


def fatal(message: str, **kwargs: Any) -> NoReturn:
	_logger_print(FATAL_LEVEL, _construct_message(message, **kwargs))
	exit(1)


def fatalf(format_str: str, *args: Any) -> NoReturn:
	_logger_print(FATAL_LEVEL, format_str.format(*args))
	exit(1)


if __name__ == "__main__":
	log("hello")
	log("this is kwargs example", hello="world")
	logf("hello {}", "world")
	debug("hello")
	debug("this is kwargs example", hello="world")
	debugf("hello {}", "world")
	info("hello")
	info("this is kwargs example", hello="world")
	infof("hello {}", "world")
	warn("hello")
	warn("this is kwargs example", hello="world")
	warnf("hello {}", "world")
	error("hello")
	error("this is kwargs example", hello="world")
	errorf("hello {}", "world")
	exit(0)
