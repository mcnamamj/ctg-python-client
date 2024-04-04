from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.flow_group import FlowGroup
    from ..models.flow_period import FlowPeriod


T = TypeVar("T", bound="ParticipantFlowModule")


@_attrs_define
class ParticipantFlowModule:
    """
    Attributes:
        pre_assignment_details (Union[Unset, str]):
        recruitment_details (Union[Unset, str]):
        type_units_analyzed (Union[Unset, str]):
        groups (Union[Unset, List['FlowGroup']]):
        periods (Union[Unset, List['FlowPeriod']]):
    """

    pre_assignment_details: Union[Unset, str] = UNSET
    recruitment_details: Union[Unset, str] = UNSET
    type_units_analyzed: Union[Unset, str] = UNSET
    groups: Union[Unset, List["FlowGroup"]] = UNSET
    periods: Union[Unset, List["FlowPeriod"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pre_assignment_details = self.pre_assignment_details

        recruitment_details = self.recruitment_details

        type_units_analyzed = self.type_units_analyzed

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        periods: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.periods, Unset):
            periods = []
            for periods_item_data in self.periods:
                periods_item = periods_item_data.to_dict()
                periods.append(periods_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pre_assignment_details is not UNSET:
            field_dict["preAssignmentDetails"] = pre_assignment_details
        if recruitment_details is not UNSET:
            field_dict["recruitmentDetails"] = recruitment_details
        if type_units_analyzed is not UNSET:
            field_dict["typeUnitsAnalyzed"] = type_units_analyzed
        if groups is not UNSET:
            field_dict["groups"] = groups
        if periods is not UNSET:
            field_dict["periods"] = periods

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.flow_group import FlowGroup
        from ..models.flow_period import FlowPeriod

        d = src_dict.copy()
        pre_assignment_details = d.pop("preAssignmentDetails", UNSET)

        recruitment_details = d.pop("recruitmentDetails", UNSET)

        type_units_analyzed = d.pop("typeUnitsAnalyzed", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = FlowGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        periods = []
        _periods = d.pop("periods", UNSET)
        for periods_item_data in _periods or []:
            periods_item = FlowPeriod.from_dict(periods_item_data)

            periods.append(periods_item)

        participant_flow_module = cls(
            pre_assignment_details=pre_assignment_details,
            recruitment_details=recruitment_details,
            type_units_analyzed=type_units_analyzed,
            groups=groups,
            periods=periods,
        )

        participant_flow_module.additional_properties = d
        return participant_flow_module

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
