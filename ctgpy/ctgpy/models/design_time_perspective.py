from enum import Enum


class DesignTimePerspective(str, Enum):
    CROSS_SECTIONAL = "CROSS_SECTIONAL"
    OTHER = "OTHER"
    PROSPECTIVE = "PROSPECTIVE"
    RETROSPECTIVE = "RETROSPECTIVE"

    def __str__(self) -> str:
        return str(self.value)
