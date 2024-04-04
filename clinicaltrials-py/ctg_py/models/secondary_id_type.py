from enum import Enum


class SecondaryIdType(str, Enum):
    AHRQ = "AHRQ"
    CDC = "CDC"
    CTIS = "CTIS"
    EUDRACT_NUMBER = "EUDRACT_NUMBER"
    FDA = "FDA"
    NIH = "NIH"
    OTHER = "OTHER"
    OTHER_GRANT = "OTHER_GRANT"
    REGISTRY = "REGISTRY"
    SAMHSA = "SAMHSA"
    VA = "VA"

    def __str__(self) -> str:
        return str(self.value)
