from enum import Enum


class RecruitmentStatus(str, Enum):
    ACTIVE_NOT_RECRUITING = "ACTIVE_NOT_RECRUITING"
    AVAILABLE = "AVAILABLE"
    COMPLETED = "COMPLETED"
    ENROLLING_BY_INVITATION = "ENROLLING_BY_INVITATION"
    NOT_YET_RECRUITING = "NOT_YET_RECRUITING"
    RECRUITING = "RECRUITING"
    SUSPENDED = "SUSPENDED"
    TERMINATED = "TERMINATED"
    WITHDRAWN = "WITHDRAWN"

    def __str__(self) -> str:
        return str(self.value)
