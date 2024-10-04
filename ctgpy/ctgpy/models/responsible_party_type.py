from enum import Enum


class ResponsiblePartyType(str, Enum):
    PRINCIPAL_INVESTIGATOR = "PRINCIPAL_INVESTIGATOR"
    SPONSOR = "SPONSOR"
    SPONSOR_INVESTIGATOR = "SPONSOR_INVESTIGATOR"

    def __str__(self) -> str:
        return str(self.value)
