from enum import Enum


class AgencyClass(str, Enum):
    AMBIG = "AMBIG"
    FED = "FED"
    INDIV = "INDIV"
    INDUSTRY = "INDUSTRY"
    NETWORK = "NETWORK"
    NIH = "NIH"
    OTHER = "OTHER"
    OTHER_GOV = "OTHER_GOV"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
