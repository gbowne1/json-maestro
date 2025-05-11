from enum import Enum
from typing import List


class Format(Enum):
    eNone = 0
    eJson = 1
    eJsonWithCommnets = 2

    @classmethod
    def count(cls) -> int:
        ...

    @classmethod
    def max(cls) -> int:
        ...

    @classmethod
    def names(cls) -> List[str]:
        ...

    @classmethod
    def get_name(cls, value: int) -> str:
        ...

    @classmethod
    def values(cls) -> List[int]:
        ...

    @classmethod
    def from_value(cls, value: int) -> 'Format':
        ...
