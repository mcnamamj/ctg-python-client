from enum import Enum


class Phase(str, Enum):
    EARLY_PHASE1 = "EARLY_PHASE1"
    NA = "NA"
    PHASE1 = "PHASE1"
    PHASE2 = "PHASE2"
    PHASE3 = "PHASE3"
    PHASE4 = "PHASE4"

    def __str__(self) -> str:
        return str(self.value)
