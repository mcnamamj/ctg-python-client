from enum import Enum


class WhoMasked(str, Enum):
    CARE_PROVIDER = "CARE_PROVIDER"
    INVESTIGATOR = "INVESTIGATOR"
    OUTCOMES_ASSESSOR = "OUTCOMES_ASSESSOR"
    PARTICIPANT = "PARTICIPANT"

    def __str__(self) -> str:
        return str(self.value)
