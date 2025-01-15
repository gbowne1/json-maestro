try:
    from .constants import NO_LEVEL, DEBUG_LEVEL, INFO_LEVEL, WARN_LEVEL, ERROR_LEVEL, FATAL_LEVEL, DEBUG_COLOR, ERROR_COLOR, FATAL_COLOR, INFO_COLOR, RESET_COLOR, WARN_COLOR
except ImportError:
    from constants import NO_LEVEL, DEBUG_LEVEL, INFO_LEVEL, WARN_LEVEL, ERROR_LEVEL, FATAL_LEVEL, DEBUG_COLOR, ERROR_COLOR, FATAL_COLOR, INFO_COLOR, RESET_COLOR, WARN_COLOR


def logger_print(level: int, message: str) -> None:
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
        return
