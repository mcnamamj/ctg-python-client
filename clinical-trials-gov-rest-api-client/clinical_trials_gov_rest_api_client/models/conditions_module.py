from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConditionsModule")


@_attrs_define
class ConditionsModule:
    """
    Attributes:
        conditions (Union[Unset, List[str]]):
        keywords (Union[Unset, List[str]]):
    """

    conditions: Union[Unset, List[str]] = UNSET
    keywords: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conditions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = self.conditions

        keywords: Union[Unset, List[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        conditions = cast(List[str], d.pop("conditions", UNSET))

        keywords = cast(List[str], d.pop("keywords", UNSET))

        conditions_module = cls(
            conditions=conditions,
            keywords=keywords,
        )

        conditions_module.additional_properties = d
        return conditions_module

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
