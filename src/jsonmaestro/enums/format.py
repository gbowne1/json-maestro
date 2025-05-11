from enum import Enum
from typing import List

from jsonmaestro.errors import InvalidArgument


class Format(Enum):
    eNone = 0
    eJson = 1
    eJsonWithCommnets = 2

    @classmethod
    def count(cls) -> int:
        return len(cls)

    @classmethod
    def max(cls) -> int:
        return max(cls.values())

    @classmethod
    def names(cls) -> List[str]:
        return [item.name for item in cls]

    @classmethod
    def get_name(cls, value: int) -> str:
        for item in cls:
            if item.value == value:
                return item.name
        raise InvalidArgument(f'Invalid value for Format: {value}')

    @classmethod
    def values(cls) -> List[int]:
        return [item.value for item in cls]

    @classmethod
    def from_value(cls, value: int) -> 'Format':
        for item in cls:
            if item.value == value:
                return item
        raise InvalidArgument(f'Invalid value for Format: {value}')
