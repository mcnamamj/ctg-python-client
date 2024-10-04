from enum import Enum


class DesignAllocation(str, Enum):
    NA = "NA"
    NON_RANDOMIZED = "NON_RANDOMIZED"
    RANDOMIZED = "RANDOMIZED"

    def __str__(self) -> str:
        return str(self.value)
