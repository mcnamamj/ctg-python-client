from enum import Enum


class ReferenceType(str, Enum):
    BACKGROUND = "BACKGROUND"
    DERIVED = "DERIVED"
    RESULT = "RESULT"

    def __str__(self) -> str:
        return str(self.value)
