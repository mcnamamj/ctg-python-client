from enum import Enum


class SamplingMethod(str, Enum):
    NON_PROBABILITY_SAMPLE = "NON_PROBABILITY_SAMPLE"
    PROBABILITY_SAMPLE = "PROBABILITY_SAMPLE"

    def __str__(self) -> str:
        return str(self.value)
