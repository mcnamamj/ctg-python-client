from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.field_stats_type import FieldStatsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.longest_string import LongestString
    from ..models.value_count import ValueCount


T = TypeVar("T", bound="StringStats")


@_attrs_define
class StringStats:
    """
    Attributes:
        field (str):
        missing_studies_count (int):
        piece (str):
        type (FieldStatsType):
        unique_values_count (int):
        longest (Union[Unset, LongestString]):
        top_values (Union[Unset, List['ValueCount']]):
    """

    field: str
    missing_studies_count: int
    piece: str
    type: FieldStatsType
    unique_values_count: int
    longest: Union[Unset, "LongestString"] = UNSET
    top_values: Union[Unset, List["ValueCount"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field = self.field

        missing_studies_count = self.missing_studies_count

        piece = self.piece

        type = self.type.value

        unique_values_count = self.unique_values_count

        longest: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.longest, Unset):
            longest = self.longest.to_dict()

        top_values: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.top_values, Unset):
            top_values = []
            for top_values_item_data in self.top_values:
                top_values_item = top_values_item_data.to_dict()
                top_values.append(top_values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "field": field,
                "missingStudiesCount": missing_studies_count,
                "piece": piece,
                "type": type,
                "uniqueValuesCount": unique_values_count,
            }
        )
        if longest is not UNSET:
            field_dict["longest"] = longest
        if top_values is not UNSET:
            field_dict["topValues"] = top_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.longest_string import LongestString
        from ..models.value_count import ValueCount

        d = src_dict.copy()
        field = d.pop("field")

        missing_studies_count = d.pop("missingStudiesCount")

        piece = d.pop("piece")

        type = FieldStatsType(d.pop("type"))

        unique_values_count = d.pop("uniqueValuesCount")

        _longest = d.pop("longest", UNSET)
        longest: Union[Unset, LongestString]
        if isinstance(_longest, Unset):
            longest = UNSET
        else:
            longest = LongestString.from_dict(_longest)

        top_values = []
        _top_values = d.pop("topValues", UNSET)
        for top_values_item_data in _top_values or []:
            top_values_item = ValueCount.from_dict(top_values_item_data)

            top_values.append(top_values_item)

        string_stats = cls(
            field=field,
            missing_studies_count=missing_studies_count,
            piece=piece,
            type=type,
            unique_values_count=unique_values_count,
            longest=longest,
            top_values=top_values,
        )

        return string_stats
