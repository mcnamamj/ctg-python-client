from enum import Enum


class DesignMasking(str, Enum):
    DOUBLE = "DOUBLE"
    NONE = "NONE"
    QUADRUPLE = "QUADRUPLE"
    SINGLE = "SINGLE"
    TRIPLE = "TRIPLE"

    def __str__(self) -> str:
        return str(self.value)
