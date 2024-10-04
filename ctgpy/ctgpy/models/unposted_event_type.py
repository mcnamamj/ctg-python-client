from enum import Enum


class UnpostedEventType(str, Enum):
    RELEASE = "RELEASE"
    RESET = "RESET"
    UNRELEASE = "UNRELEASE"

    def __str__(self) -> str:
        return str(self.value)
