from enum import Enum


class IpdSharingInfoType(str, Enum):
    ANALYTIC_CODE = "ANALYTIC_CODE"
    CSR = "CSR"
    ICF = "ICF"
    SAP = "SAP"
    STUDY_PROTOCOL = "STUDY_PROTOCOL"

    def __str__(self) -> str:
        return str(self.value)
