from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..models.field_stats_type import FieldStatsType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.value_count import ValueCount


T = TypeVar("T", bound="EnumStats")


@_attrs_define
class EnumStats:
    """
    Attributes:
        field (str):
        missing_studies_count (int):
        piece (str):
        type (FieldStatsType):
        unique_values_count (int):
        top_values (Union[Unset, List['ValueCount']]):
    """

    field: str
    missing_studies_count: int
    piece: str
    type: FieldStatsType
    unique_values_count: int
    top_values: Union[Unset, List["ValueCount"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field = self.field

        missing_studies_count = self.missing_studies_count

        piece = self.piece

        type = self.type.value

        unique_values_count = self.unique_values_count

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
        if top_values is not UNSET:
            field_dict["topValues"] = top_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.value_count import ValueCount

        d = src_dict.copy()
        field = d.pop("field")

        missing_studies_count = d.pop("missingStudiesCount")

        piece = d.pop("piece")

        type = FieldStatsType(d.pop("type"))

        unique_values_count = d.pop("uniqueValuesCount")

        top_values = []
        _top_values = d.pop("topValues", UNSET)
        for top_values_item_data in _top_values or []:
            top_values_item = ValueCount.from_dict(top_values_item_data)

            top_values.append(top_values_item)

        enum_stats = cls(
            field=field,
            missing_studies_count=missing_studies_count,
            piece=piece,
            type=type,
            unique_values_count=unique_values_count,
            top_values=top_values,
        )

        return enum_stats
