from enum import Enum


class InterventionType(str, Enum):
    BEHAVIORAL = "BEHAVIORAL"
    BIOLOGICAL = "BIOLOGICAL"
    COMBINATION_PRODUCT = "COMBINATION_PRODUCT"
    DEVICE = "DEVICE"
    DIAGNOSTIC_TEST = "DIAGNOSTIC_TEST"
    DIETARY_SUPPLEMENT = "DIETARY_SUPPLEMENT"
    DRUG = "DRUG"
    GENETIC = "GENETIC"
    OTHER = "OTHER"
    PROCEDURE = "PROCEDURE"
    RADIATION = "RADIATION"

    def __str__(self) -> str:
        return str(self.value)
