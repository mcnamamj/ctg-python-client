from enum import Enum


class OutcomeMeasureType(str, Enum):
    OTHER_PRE_SPECIFIED = "OTHER_PRE_SPECIFIED"
    POST_HOC = "POST_HOC"
    PRIMARY = "PRIMARY"
    SECONDARY = "SECONDARY"

    def __str__(self) -> str:
        return str(self.value)
