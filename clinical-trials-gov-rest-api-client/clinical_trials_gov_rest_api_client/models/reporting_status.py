from enum import Enum


class ReportingStatus(str, Enum):
    NOT_POSTED = "NOT_POSTED"
    POSTED = "POSTED"

    def __str__(self) -> str:
        return str(self.value)
