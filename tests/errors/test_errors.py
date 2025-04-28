from typing import Union

import pytest

from jsonmaestro.errors import IError, Error, InvalidArgument


# Tests for IError
def test_ierror_initialization():
    with pytest.raises(NotImplementedError):
        IError("Test message")


def test_ierror_str():

    class ConcreteIError(IError):

        def __init__(self, p_message: str, p_name: Union[str, None] = None):
            self.message = p_message
            self.name = p_name

    error = ConcreteIError("Test message")
    with pytest.raises(NotImplementedError):
        str(error)


def test_ierror_repr():

    class ConcreteIError(IError):

        def __init__(self, p_message: str, p_name: Union[str, None] = None):
            self.message = p_message
            self.name = p_name

    error = ConcreteIError("Test message")
    with pytest.raises(NotImplementedError):
        repr(error)


def test_ierror_what():

    class ConcreteIError(IError):

        def __init__(self, p_message: str, p_name: Union[str, None] = None):
            self.message = p_message
            self.name = p_name

    error = ConcreteIError("Test message")
    with pytest.raises(NotImplementedError):
        error.what()


# Tests for Error
def test_error_initialization():
    error = Error("Test message")
    # We are testing the member variables
    assert error.message == "Test message"  # type: ignore
    assert error.name is None  # type: ignore


def test_error_initialization_with_name():
    error = Error("Test message", p_name="TestError")
    # We are testing the member variables
    assert error.message == "Test message"  # type: ignore
    assert error.name == "TestError"  # type: ignore


def test_error_str():
    error = Error("Test message")
    assert str(error) == "Error: Test message"

    error_with_name = Error("Test message", p_name="TestError")
    assert str(error_with_name) == "Error(TestError): Test message"


def test_error_repr():
    error = Error("Test message")
    assert repr(error) == "(name: None, message: Test message)"

    error_with_name = Error("Test message", p_name="TestError")
    assert repr(error_with_name) == "(name: TestError, message: Test message)"


def test_error_what():
    error = Error("Test message")
    assert error.what() == "Test message"


def test_error_inheritance():
    error = Error("Test message")
    assert isinstance(error, Exception)


def test_error_raises():
    with pytest.raises(Error) as excinfo:
        raise Error("Test message")
    assert str(excinfo.value) == "Error: Test message"

    with pytest.raises(Error) as excinfo:
        raise Error("Test message", p_name="TestError")
    assert str(excinfo.value) == "Error(TestError): Test message"


# Tests for InvalidArgument
def test_invalid_argument_initialization():
    error = InvalidArgument("Test message")
    # We are testing the member variables
    assert error.message == "Test message"  # type: ignore
    assert error.name == "InvalidArgument"  # type: ignore


def test_invalid_argument_str():
    error = InvalidArgument("Test message")
    assert str(error) == "Error(InvalidArgument): Test message"


def test_invalid_argument_repr():
    error = InvalidArgument("Test message")
    assert repr(error) == "(name: InvalidArgument, message: Test message)"


def test_invalid_argument_what():
    error = InvalidArgument("Test message")
    assert error.what() == "Test message"


def test_invalid_argument_inheritance():
    error = InvalidArgument("Test message")
    assert isinstance(error, Error)
    assert isinstance(error, IError)


def test_invalid_argument_raises():
    with pytest.raises(InvalidArgument) as excinfo:
        raise InvalidArgument("Test message")
    assert str(excinfo.value) == "Error(InvalidArgument): Test message"
