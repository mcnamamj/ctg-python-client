from enum import Enum


class OrgStudyIdType(str, Enum):
    AHRQ = "AHRQ"
    CDC = "CDC"
    FDA = "FDA"
    NIH = "NIH"
    SAMHSA = "SAMHSA"
    VA = "VA"

    def __str__(self) -> str:
        return str(self.value)
