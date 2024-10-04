from enum import Enum


class ObservationalModel(str, Enum):
    CASE_CONTROL = "CASE_CONTROL"
    CASE_CROSSOVER = "CASE_CROSSOVER"
    CASE_ONLY = "CASE_ONLY"
    COHORT = "COHORT"
    DEFINED_POPULATION = "DEFINED_POPULATION"
    ECOLOGIC_OR_COMMUNITY = "ECOLOGIC_OR_COMMUNITY"
    FAMILY_BASED = "FAMILY_BASED"
    NATURAL_HISTORY = "NATURAL_HISTORY"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
