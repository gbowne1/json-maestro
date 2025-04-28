from typing import Union


class IError(Exception):

    def __init__(self,
                 p_message: str,
                 p_name: Union[str, None] = None) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def what(self) -> str:
        ...


class Error(Exception):

    def __init__(self,
                 p_message: str,
                 p_name: Union[str, None] = None) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def what(self) -> str:
        ...


class InvalidArgument(Error):

    def __init__(self, p_message: str) -> None:
        ...


__all__ = ["Error", "InvalidArgument"]
