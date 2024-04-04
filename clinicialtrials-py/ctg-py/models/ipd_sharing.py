from enum import Enum


class IpdSharing(str, Enum):
    NO = "NO"
    UNDECIDED = "UNDECIDED"
    YES = "YES"

    def __str__(self) -> str:
        return str(self.value)
