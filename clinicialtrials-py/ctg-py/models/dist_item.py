from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DistItem")


@_attrs_define
class DistItem:
    """
    Attributes:
        size_range (str):
        studies_count (int):
    """

    size_range: str
    studies_count: int

    def to_dict(self) -> Dict[str, Any]:
        size_range = self.size_range

        studies_count = self.studies_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "sizeRange": size_range,
                "studiesCount": studies_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        size_range = d.pop("sizeRange")

        studies_count = d.pop("studiesCount")

        dist_item = cls(
            size_range=size_range,
            studies_count=studies_count,
        )

        return dist_item
