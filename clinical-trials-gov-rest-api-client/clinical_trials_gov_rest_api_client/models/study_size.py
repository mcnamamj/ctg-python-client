from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="StudySize")


@_attrs_define
class StudySize:
    """
    Attributes:
        id (str):
        size_bytes (int):
    """

    id: str
    size_bytes: int

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        size_bytes = self.size_bytes

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "id": id,
                "sizeBytes": size_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        size_bytes = d.pop("sizeBytes")

        study_size = cls(
            id=id,
            size_bytes=size_bytes,
        )

        return study_size
