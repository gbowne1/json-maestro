from typing import Union


class IError(Exception):
    """
    Interface for all errors.
    """

    def __init__(self,
                 p_message: str,
                 p_name: Union[str, None] = None) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def what(self) -> str:
        raise NotImplementedError


class Error(IError):
    """
    Base class for all errors.
    """

    name: Union[str, None]
    message: str

    def __init__(self,
                 p_message: str,
                 p_name: Union[str, None] = None) -> None:
        """
        Initializes the error.

        :param p_message: The error message.
        :type p_message: str
        """
        self.message = p_message
        self.name = p_name

    def __str__(self) -> str:
        if self.name is None:
            return f"Error: {self.message}"
        return f"Error({self.name}): {self.message}"

    def __repr__(self) -> str:
        name = self.name if self.name is not None else "None"
        return f"(name: {name}, message: {self.message})"

    def what(self) -> str:
        return self.message


class InvalidArgument(Error):
    """
    Raised when an argument is invalid.
    """

    def __init__(self, p_message: str) -> None:
        """
        Initializes the error.

        :param p_message: The error message.
        :type p_message: str
        """
        super().__init__(p_message, "InvalidArgument")


__all__ = ["IError", "Error", "InvalidArgument"]
