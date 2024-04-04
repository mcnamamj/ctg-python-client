from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Measurement")


@_attrs_define
class Measurement:
    """
    Attributes:
        group_id (Union[Unset, str]):
        value (Union[Unset, str]):
        spread (Union[Unset, str]):
        lower_limit (Union[Unset, str]):
        upper_limit (Union[Unset, str]):
        comment (Union[Unset, str]):
    """

    group_id: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    spread: Union[Unset, str] = UNSET
    lower_limit: Union[Unset, str] = UNSET
    upper_limit: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id

        value = self.value

        spread = self.spread

        lower_limit = self.lower_limit

        upper_limit = self.upper_limit

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if value is not UNSET:
            field_dict["value"] = value
        if spread is not UNSET:
            field_dict["spread"] = spread
        if lower_limit is not UNSET:
            field_dict["lowerLimit"] = lower_limit
        if upper_limit is not UNSET:
            field_dict["upperLimit"] = upper_limit
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("groupId", UNSET)

        value = d.pop("value", UNSET)

        spread = d.pop("spread", UNSET)

        lower_limit = d.pop("lowerLimit", UNSET)

        upper_limit = d.pop("upperLimit", UNSET)

        comment = d.pop("comment", UNSET)

        measurement = cls(
            group_id=group_id,
            value=value,
            spread=spread,
            lower_limit=lower_limit,
            upper_limit=upper_limit,
            comment=comment,
        )

        measurement.additional_properties = d
        return measurement

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
