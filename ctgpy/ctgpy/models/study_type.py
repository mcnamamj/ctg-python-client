from enum import Enum


class StudyType(str, Enum):
    EXPANDED_ACCESS = "EXPANDED_ACCESS"
    INTERVENTIONAL = "INTERVENTIONAL"
    OBSERVATIONAL = "OBSERVATIONAL"

    def __str__(self) -> str:
        return str(self.value)
