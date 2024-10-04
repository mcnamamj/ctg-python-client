from enum import Enum


class FieldStatsType(str, Enum):
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    ENUM = "ENUM"
    INTEGER = "INTEGER"
    NUMBER = "NUMBER"
    STRING = "STRING"

    def __str__(self) -> str:
        return str(self.value)
