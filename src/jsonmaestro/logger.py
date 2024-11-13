from typing import Any

NO_LEVEL = -1
DEBUG_LEVEL = 0
INFO_LEVEL = 1
WARN_LEVEL = 2
ERROR_LEVEL = 3
FATAL_LEVEL = 4

RESET_COLOR = "\033[0m"
DEBUG_COLOR = "\033[94m"  # Bright Blue
INFO_COLOR = "\033[92m"  # Bright Green
WARN_COLOR = "\033[93m"  # Bright Yellow
ERROR_COLOR = "\033[91m"  # Bright Red
FATAL_COLOR = "\033[95m"  # Bright Magenta


# For match we need 3.10
def logger_print(level: int, message: str):
	if level is NO_LEVEL:
		print(message)
		return
	if level is DEBUG_LEVEL:
		print(f"{DEBUG_COLOR}[ DEBUG ]{RESET_COLOR}: {message}")
		return
	if level is INFO_LEVEL:
		print(f"{INFO_COLOR}[ INFO ]{RESET_COLOR}: {message}")
		return
	if level is WARN_LEVEL:
		print(f"{WARN_COLOR}[ WARN ]{RESET_COLOR}: {message}")
		return
	if level is ERROR_LEVEL:
		print(f"{ERROR_COLOR}[ ERROR ]{RESET_COLOR}: {message}")
		return
	if level is FATAL_LEVEL:
		print(f"{FATAL_COLOR}[ FATAL ]{RESET_COLOR}: {message}")
		exit(1)


def construct_message(message: str, **kwargs: dict[Any, Any]) -> str:
	if kwargs:
		context_mesage = "".join(
		    f"\t{key}={value}\n"
		    for key, value in kwargs.items()).removesuffix("\n")
		return f"{message} |\n{context_mesage}"
	else:
		return message


def log(message: str, **kwargs: dict[Any, Any]):
	logger_print(NO_LEVEL, construct_message(message, **kwargs))


def debug(message: str, **kwargs: dict[Any, Any]):
	logger_print(DEBUG_LEVEL, construct_message(message, **kwargs))


def info(message: str, **kwargs: dict[Any, Any]):
	logger_print(INFO_LEVEL, construct_message(message, **kwargs))


def warn(message: str, **kwargs: dict[Any, Any]):
	logger_print(WARN_LEVEL, construct_message(message, **kwargs))


def error(message: str, **kwargs: dict[Any, Any]):
	logger_print(ERROR_LEVEL, construct_message(message, **kwargs))


def fatal(message: str, **kwargs: dict[Any, Any]):
	logger_print(FATAL_LEVEL, construct_message(message, **kwargs))


if __name__ == "__main__":
	log("hello")
	log("this is kwargs example", hello="world")
	debug("hello")
	debug("this is kwargs example", hello="world")
	info("hello")
	info("this is kwargs example", hello="world")
	warn("hello")
	warn("this is kwargs example", hello="world")
	error("hello")
	error("this is kwargs example", hello="world")
	exit(0)
