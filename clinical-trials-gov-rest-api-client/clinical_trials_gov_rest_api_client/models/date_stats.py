from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.field_stats_type import FieldStatsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DateStats")


@_attrs_define
class DateStats:
    """
    Attributes:
        field (str):
        formats (List[str]):
        missing_studies_count (int):
        piece (str):
        type (FieldStatsType):
        max_ (Union[Unset, str]):
        min_ (Union[Unset, str]):
    """

    field: str
    formats: List[str]
    missing_studies_count: int
    piece: str
    type: FieldStatsType
    max_: Union[Unset, str] = UNSET
    min_: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field = self.field

        formats = self.formats

        missing_studies_count = self.missing_studies_count

        piece = self.piece

        type = self.type.value

        max_ = self.max_

        min_ = self.min_

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "field": field,
                "formats": formats,
                "missingStudiesCount": missing_studies_count,
                "piece": piece,
                "type": type,
            }
        )
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field = d.pop("field")

        formats = cast(List[str], d.pop("formats"))

        missing_studies_count = d.pop("missingStudiesCount")

        piece = d.pop("piece")

        type = FieldStatsType(d.pop("type"))

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        date_stats = cls(
            field=field,
            formats=formats,
            missing_studies_count=missing_studies_count,
            piece=piece,
            type=type,
            max_=max_,
            min_=min_,
        )

        return date_stats
