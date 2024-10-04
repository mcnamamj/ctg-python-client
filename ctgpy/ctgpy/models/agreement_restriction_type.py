from enum import Enum


class AgreementRestrictionType(str, Enum):
    GT60 = "GT60"
    LTE60 = "LTE60"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
