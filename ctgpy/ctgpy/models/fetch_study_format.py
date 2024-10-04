from enum import Enum


class FetchStudyFormat(str, Enum):
    CSV = "csv"
    FHIR_JSON = "fhir.json"
    JSON = "json"
    JSON_ZIP = "json.zip"

    def __str__(self) -> str:
        return str(self.value)
