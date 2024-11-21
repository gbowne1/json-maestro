from typing import Any, NoReturn

_NO_LEVEL = -1
_DEBUG_LEVEL = 0
_INFO_LEVEL = 1
_WARN_LEVEL = 2
_ERROR_LEVEL = 3
_FATAL_LEVEL = 4

_RESET_COLOR = "\033[0m"
_DEBUG_COLOR = "\033[94m"  # Bright Blue
_INFO_COLOR = "\033[92m"  # Bright Green
_WARN_COLOR = "\033[93m"  # Bright Yellow
_ERROR_COLOR = "\033[91m"  # Bright Red
_FATAL_COLOR = "\033[95m"  # Bright Magenta


# For match we need 3.10
def _logger_print(level: int, message: str):
	if level is _NO_LEVEL:
		print(message)
		return
	if level is _DEBUG_LEVEL:
		print(f"{_DEBUG_COLOR}[ DEBUG ]{_RESET_COLOR}: {message}")
		return
	if level is _INFO_LEVEL:
		print(f"{_INFO_COLOR}[ INFO ]{_RESET_COLOR}: {message}")
		return
	if level is _WARN_LEVEL:
		print(f"{_WARN_COLOR}[ WARN ]{_RESET_COLOR}: {message}")
		return
	if level is _ERROR_LEVEL:
		print(f"{_ERROR_COLOR}[ ERROR ]{_RESET_COLOR}: {message}")
		return
	if level is _FATAL_LEVEL:
		print(f"{_FATAL_COLOR}[ FATAL ]{_RESET_COLOR}: {message}")


def _construct_message(message: str, **kwargs: Any) -> str:
	if kwargs:
		context_mesage = "".join(
		    f"\t{key}={value}\n"
		    for key, value in kwargs.items()).removesuffix("\n")
		return f"{message} |\n{context_mesage}"
	else:
		return message


def log(message: str, **kwargs: Any):
	_logger_print(_NO_LEVEL, _construct_message(message, **kwargs))


def logf(format_str: str, *args: Any):
	_logger_print(_NO_LEVEL, _construct_message(format_str.format(*args)))


def debug(message: str, **kwargs: Any):
	_logger_print(_DEBUG_LEVEL, _construct_message(message, **kwargs))


def debugf(format_str: str, *args: Any):
	_logger_print(_DEBUG_LEVEL, format_str.format(*args))


def info(message: str, **kwargs: Any):
	_logger_print(_INFO_LEVEL, _construct_message(message, **kwargs))


def infof(format_str: str, *args: Any):
	_logger_print(_INFO_LEVEL, format_str.format(*args))


def warn(message: str, **kwargs: Any):
	_logger_print(_WARN_LEVEL, _construct_message(message, **kwargs))


def warnf(format_str: str, *args: Any):
	_logger_print(_WARN_LEVEL, format_str.format(*args))


def error(message: str, **kwargs: Any):
	_logger_print(_ERROR_LEVEL, _construct_message(message, **kwargs))


def errorf(format_str: str, *args: Any):
	_logger_print(_ERROR_LEVEL, format_str.format(*args))


def fatal(message: str, **kwargs: Any) -> NoReturn:
	_logger_print(_FATAL_LEVEL, _construct_message(message, **kwargs))
	exit(1)


def fatalf(format_str: str, *args: Any) -> NoReturn:
	_logger_print(_FATAL_LEVEL, format_str.format(*args))
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
