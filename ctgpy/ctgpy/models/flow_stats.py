from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlowStats")


@_attrs_define
class FlowStats:
    """
    Attributes:
        group_id (Union[Unset, str]):
        comment (Union[Unset, str]):
        num_subjects (Union[Unset, str]):
        num_units (Union[Unset, str]):
    """

    group_id: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    num_subjects: Union[Unset, str] = UNSET
    num_units: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id

        comment = self.comment

        num_subjects = self.num_subjects

        num_units = self.num_units

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if num_subjects is not UNSET:
            field_dict["numSubjects"] = num_subjects
        if num_units is not UNSET:
            field_dict["numUnits"] = num_units

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("groupId", UNSET)

        comment = d.pop("comment", UNSET)

        num_subjects = d.pop("numSubjects", UNSET)

        num_units = d.pop("numUnits", UNSET)

        flow_stats = cls(
            group_id=group_id,
            comment=comment,
            num_subjects=num_subjects,
            num_units=num_units,
        )

        flow_stats.additional_properties = d
        return flow_stats

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
