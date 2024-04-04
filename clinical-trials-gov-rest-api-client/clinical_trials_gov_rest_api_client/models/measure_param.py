from enum import Enum


class MeasureParam(str, Enum):
    COUNT_OF_PARTICIPANTS = "COUNT_OF_PARTICIPANTS"
    COUNT_OF_UNITS = "COUNT_OF_UNITS"
    GEOMETRIC_LEAST_SQUARES_MEAN = "GEOMETRIC_LEAST_SQUARES_MEAN"
    GEOMETRIC_MEAN = "GEOMETRIC_MEAN"
    LEAST_SQUARES_MEAN = "LEAST_SQUARES_MEAN"
    LOG_MEAN = "LOG_MEAN"
    MEAN = "MEAN"
    MEDIAN = "MEDIAN"
    NUMBER = "NUMBER"

    def __str__(self) -> str:
        return str(self.value)
