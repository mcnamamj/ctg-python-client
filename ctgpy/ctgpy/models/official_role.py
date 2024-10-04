from enum import Enum


class OfficialRole(str, Enum):
    PRINCIPAL_INVESTIGATOR = "PRINCIPAL_INVESTIGATOR"
    STUDY_CHAIR = "STUDY_CHAIR"
    STUDY_DIRECTOR = "STUDY_DIRECTOR"
    SUB_INVESTIGATOR = "SUB_INVESTIGATOR"

    def __str__(self) -> str:
        return str(self.value)
