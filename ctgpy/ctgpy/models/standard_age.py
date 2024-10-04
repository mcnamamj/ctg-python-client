from enum import Enum


class StandardAge(str, Enum):
    ADULT = "ADULT"
    CHILD = "CHILD"
    OLDER_ADULT = "OLDER_ADULT"

    def __str__(self) -> str:
        return str(self.value)
