from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.arm_group import ArmGroup
    from ..models.intervention import Intervention


T = TypeVar("T", bound="ArmsInterventionsModule")


@_attrs_define
class ArmsInterventionsModule:
    """
    Attributes:
        arm_groups (Union[Unset, List['ArmGroup']]):
        interventions (Union[Unset, List['Intervention']]):
    """

    arm_groups: Union[Unset, List["ArmGroup"]] = UNSET
    interventions: Union[Unset, List["Intervention"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        arm_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.arm_groups, Unset):
            arm_groups = []
            for arm_groups_item_data in self.arm_groups:
                arm_groups_item = arm_groups_item_data.to_dict()
                arm_groups.append(arm_groups_item)

        interventions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interventions, Unset):
            interventions = []
            for interventions_item_data in self.interventions:
                interventions_item = interventions_item_data.to_dict()
                interventions.append(interventions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arm_groups is not UNSET:
            field_dict["armGroups"] = arm_groups
        if interventions is not UNSET:
            field_dict["interventions"] = interventions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.arm_group import ArmGroup
        from ..models.intervention import Intervention

        d = src_dict.copy()
        arm_groups = []
        _arm_groups = d.pop("armGroups", UNSET)
        for arm_groups_item_data in _arm_groups or []:
            arm_groups_item = ArmGroup.from_dict(arm_groups_item_data)

            arm_groups.append(arm_groups_item)

        interventions = []
        _interventions = d.pop("interventions", UNSET)
        for interventions_item_data in _interventions or []:
            interventions_item = Intervention.from_dict(interventions_item_data)

            interventions.append(interventions_item)

        arms_interventions_module = cls(
            arm_groups=arm_groups,
            interventions=interventions,
        )

        arms_interventions_module.additional_properties = d
        return arms_interventions_module

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
