import pytest

from jsonmaestro.enums.format import Format
from jsonmaestro.errors import InvalidArgument


def test_enum_members():
    assert Format.eNone.value == 0
    assert Format.eJson.value == 1
    assert Format.eJsonWithCommnets.value == 2


def test_count():
    assert Format.count() == 3


def test_max():
    assert Format.max() == Format.count() - 1


def test_names():
    assert Format.names() == ['eNone', 'eJson', 'eJsonWithCommnets']


def test_get_name():
    assert Format.get_name(0) == 'eNone'
    assert Format.get_name(1) == 'eJson'
    assert Format.get_name(2) == 'eJsonWithCommnets'

    with pytest.raises(InvalidArgument) as exc_info:
        Format.get_name(99)
    assert 'Invalid value for Format: 99' in str(exc_info.value)


def test_values():
    assert Format.values() == [0, 1, 2]


def test_from_value_valid():
    assert Format.from_value(0) == Format.eNone
    assert Format.from_value(1) == Format.eJson
    assert Format.from_value(2) == Format.eJsonWithCommnets


def test_from_value_invalid():
    with pytest.raises(InvalidArgument) as exc_info:
        Format.from_value(99)
    assert 'Invalid value for Format: 99' in str(exc_info.value)
