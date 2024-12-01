try:
	from .contantants import DEBUG_COLOR, ERROR_COLOR, FATAL_COLOR, INFO_COLOR, RESET_COLOR, WARN_COLOR
except ImportError:
	from contantants import DEBUG_COLOR, ERROR_COLOR, FATAL_COLOR, INFO_COLOR, RESET_COLOR, WARN_COLOR


def logger_print(level: int, message: str) -> None:
	match level:
		case -1:
			print(message)
		case 0:
			print(f"{DEBUG_COLOR}[ DEBUG ]{RESET_COLOR}: {message}")
		case 1:
			print(f"{INFO_COLOR}[ INFO ]{RESET_COLOR}: {message}")
		case 2:
			print(f"{WARN_COLOR}[ WARN ]{RESET_COLOR}: {message}")
		case 3:
			print(f"{ERROR_COLOR}[ ERROR ]{RESET_COLOR}: {message}")
		case 4:
			print(f"{FATAL_COLOR}[ FATAL ]{RESET_COLOR}: {message}")
		case _:
			# Default case if no level matches
			print(message)
	return
