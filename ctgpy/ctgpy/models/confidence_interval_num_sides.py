from enum import Enum


class ConfidenceIntervalNumSides(str, Enum):
    ONE_SIDED = "ONE_SIDED"
    TWO_SIDED = "TWO_SIDED"

    def __str__(self) -> str:
        return str(self.value)
