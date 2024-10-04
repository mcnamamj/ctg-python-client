from enum import Enum


class BioSpecRetention(str, Enum):
    NONE_RETAINED = "NONE_RETAINED"
    SAMPLES_WITHOUT_DNA = "SAMPLES_WITHOUT_DNA"
    SAMPLES_WITH_DNA = "SAMPLES_WITH_DNA"

    def __str__(self) -> str:
        return str(self.value)
