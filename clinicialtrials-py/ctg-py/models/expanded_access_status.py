from enum import Enum


class ExpandedAccessStatus(str, Enum):
    APPROVED_FOR_MARKETING = "APPROVED_FOR_MARKETING"
    AVAILABLE = "AVAILABLE"
    NO_LONGER_AVAILABLE = "NO_LONGER_AVAILABLE"
    TEMPORARILY_NOT_AVAILABLE = "TEMPORARILY_NOT_AVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
