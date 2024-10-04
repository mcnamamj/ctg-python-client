from enum import Enum


class EnrollmentType(str, Enum):
    ACTUAL = "ACTUAL"
    ESTIMATED = "ESTIMATED"

    def __str__(self) -> str:
        return str(self.value)
