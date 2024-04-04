from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DescriptionModule")


@_attrs_define
class DescriptionModule:
    """
    Attributes:
        brief_summary (Union[Unset, str]):
        detailed_description (Union[Unset, str]):
    """

    brief_summary: Union[Unset, str] = UNSET
    detailed_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        brief_summary = self.brief_summary

        detailed_description = self.detailed_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if brief_summary is not UNSET:
            field_dict["briefSummary"] = brief_summary
        if detailed_description is not UNSET:
            field_dict["detailedDescription"] = detailed_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        brief_summary = d.pop("briefSummary", UNSET)

        detailed_description = d.pop("detailedDescription", UNSET)

        description_module = cls(
            brief_summary=brief_summary,
            detailed_description=detailed_description,
        )

        description_module.additional_properties = d
        return description_module

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
