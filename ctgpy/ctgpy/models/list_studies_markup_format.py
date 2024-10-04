from enum import Enum


class ListStudiesMarkupFormat(str, Enum):
    LEGACY = "legacy"
    MARKDOWN = "markdown"

    def __str__(self) -> str:
        return str(self.value)
