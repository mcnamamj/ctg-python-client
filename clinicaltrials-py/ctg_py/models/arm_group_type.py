from enum import Enum


class ArmGroupType(str, Enum):
    ACTIVE_COMPARATOR = "ACTIVE_COMPARATOR"
    EXPERIMENTAL = "EXPERIMENTAL"
    NO_INTERVENTION = "NO_INTERVENTION"
    OTHER = "OTHER"
    PLACEBO_COMPARATOR = "PLACEBO_COMPARATOR"
    SHAM_COMPARATOR = "SHAM_COMPARATOR"

    def __str__(self) -> str:
        return str(self.value)
