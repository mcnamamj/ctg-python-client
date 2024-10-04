from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventStats")


@_attrs_define
class EventStats:
    """
    Attributes:
        group_id (Union[Unset, str]):
        num_events (Union[Unset, int]):
        num_affected (Union[Unset, int]):
        num_at_risk (Union[Unset, int]):
    """

    group_id: Union[Unset, str] = UNSET
    num_events: Union[Unset, int] = UNSET
    num_affected: Union[Unset, int] = UNSET
    num_at_risk: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id

        num_events = self.num_events

        num_affected = self.num_affected

        num_at_risk = self.num_at_risk

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if num_events is not UNSET:
            field_dict["numEvents"] = num_events
        if num_affected is not UNSET:
            field_dict["numAffected"] = num_affected
        if num_at_risk is not UNSET:
            field_dict["numAtRisk"] = num_at_risk

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("groupId", UNSET)

        num_events = d.pop("numEvents", UNSET)

        num_affected = d.pop("numAffected", UNSET)

        num_at_risk = d.pop("numAtRisk", UNSET)

        event_stats = cls(
            group_id=group_id,
            num_events=num_events,
            num_affected=num_affected,
            num_at_risk=num_at_risk,
        )

        event_stats.additional_properties = d
        return event_stats

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
