from enum import Enum


class InterventionalAssignment(str, Enum):
    CROSSOVER = "CROSSOVER"
    FACTORIAL = "FACTORIAL"
    PARALLEL = "PARALLEL"
    SEQUENTIAL = "SEQUENTIAL"
    SINGLE_GROUP = "SINGLE_GROUP"

    def __str__(self) -> str:
        return str(self.value)
