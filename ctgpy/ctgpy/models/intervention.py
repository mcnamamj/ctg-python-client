from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.intervention_type import InterventionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Intervention")


@_attrs_define
class Intervention:
    """
    Attributes:
        type (Union[Unset, InterventionType]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        arm_group_labels (Union[Unset, List[str]]):
        other_names (Union[Unset, List[str]]):
    """

    type: Union[Unset, InterventionType] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    arm_group_labels: Union[Unset, List[str]] = UNSET
    other_names: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        name = self.name

        description = self.description

        arm_group_labels: Union[Unset, List[str]] = UNSET
        if not isinstance(self.arm_group_labels, Unset):
            arm_group_labels = self.arm_group_labels

        other_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.other_names, Unset):
            other_names = self.other_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if arm_group_labels is not UNSET:
            field_dict["armGroupLabels"] = arm_group_labels
        if other_names is not UNSET:
            field_dict["otherNames"] = other_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, InterventionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = InterventionType(_type)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        arm_group_labels = cast(List[str], d.pop("armGroupLabels", UNSET))

        other_names = cast(List[str], d.pop("otherNames", UNSET))

        intervention = cls(
            type=type,
            name=name,
            description=description,
            arm_group_labels=arm_group_labels,
            other_names=other_names,
        )

        intervention.additional_properties = d
        return intervention

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
