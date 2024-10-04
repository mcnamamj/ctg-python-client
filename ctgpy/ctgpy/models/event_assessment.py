from enum import Enum


class EventAssessment(str, Enum):
    NON_SYSTEMATIC_ASSESSMENT = "NON_SYSTEMATIC_ASSESSMENT"
    SYSTEMATIC_ASSESSMENT = "SYSTEMATIC_ASSESSMENT"

    def __str__(self) -> str:
        return str(self.value)
