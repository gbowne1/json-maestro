import pytest

from jsonmaestro.enums.format import Fromat
from jsonmaestro.errors import InvalidArgument


def test_enum_members():
    assert Fromat.eNone.value == 0
    assert Fromat.eJson.value == 1
    assert Fromat.eJsonWithCommnets.value == 2


def test_count():
    assert Fromat.count() == 3


def test_max():
    assert Fromat.max() == Fromat.count() - 1


def test_names():
    assert Fromat.names() == ['eNone', 'eJson', 'eJsonWithCommnets']


def test_get_name():
    assert Fromat.get_name(0) == 'eNone'
    assert Fromat.get_name(1) == 'eJson'
    assert Fromat.get_name(2) == 'eJsonWithCommnets'

    with pytest.raises(InvalidArgument) as exc_info:
        Fromat.get_name(99)
    assert 'Invalid value for Fromat: 99' in str(exc_info.value)


def test_values():
    assert Fromat.values() == [0, 1, 2]


def test_from_value_valid():
    assert Fromat.from_value(0) == Fromat.eNone
    assert Fromat.from_value(1) == Fromat.eJson
    assert Fromat.from_value(2) == Fromat.eJsonWithCommnets


def test_from_value_invalid():
    with pytest.raises(InvalidArgument) as exc_info:
        Fromat.from_value(99)
    assert 'Invalid value for Fromat: 99' in str(exc_info.value)
