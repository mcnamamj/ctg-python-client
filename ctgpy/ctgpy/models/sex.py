from enum import Enum


class Sex(str, Enum):
    ALL = "ALL"
    FEMALE = "FEMALE"
    MALE = "MALE"

    def __str__(self) -> str:
        return str(self.value)
