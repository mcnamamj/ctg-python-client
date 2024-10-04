from enum import Enum


class AnalysisDispersionType(str, Enum):
    STANDARD_DEVIATION = "STANDARD_DEVIATION"
    STANDARD_ERROR_OF_MEAN = "STANDARD_ERROR_OF_MEAN"

    def __str__(self) -> str:
        return str(self.value)
