from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adverse_event import AdverseEvent
    from ..models.event_group import EventGroup


T = TypeVar("T", bound="AdverseEventsModule")


@_attrs_define
class AdverseEventsModule:
    """
    Attributes:
        frequency_threshold (Union[Unset, str]):
        time_frame (Union[Unset, str]):
        description (Union[Unset, str]):
        all_cause_mortality_comment (Union[Unset, str]):
        event_groups (Union[Unset, List['EventGroup']]):
        serious_events (Union[Unset, List['AdverseEvent']]):
        other_events (Union[Unset, List['AdverseEvent']]):
    """

    frequency_threshold: Union[Unset, str] = UNSET
    time_frame: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    all_cause_mortality_comment: Union[Unset, str] = UNSET
    event_groups: Union[Unset, List["EventGroup"]] = UNSET
    serious_events: Union[Unset, List["AdverseEvent"]] = UNSET
    other_events: Union[Unset, List["AdverseEvent"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        frequency_threshold = self.frequency_threshold

        time_frame = self.time_frame

        description = self.description

        all_cause_mortality_comment = self.all_cause_mortality_comment

        event_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.event_groups, Unset):
            event_groups = []
            for event_groups_item_data in self.event_groups:
                event_groups_item = event_groups_item_data.to_dict()
                event_groups.append(event_groups_item)

        serious_events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.serious_events, Unset):
            serious_events = []
            for serious_events_item_data in self.serious_events:
                serious_events_item = serious_events_item_data.to_dict()
                serious_events.append(serious_events_item)

        other_events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.other_events, Unset):
            other_events = []
            for other_events_item_data in self.other_events:
                other_events_item = other_events_item_data.to_dict()
                other_events.append(other_events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if frequency_threshold is not UNSET:
            field_dict["frequencyThreshold"] = frequency_threshold
        if time_frame is not UNSET:
            field_dict["timeFrame"] = time_frame
        if description is not UNSET:
            field_dict["description"] = description
        if all_cause_mortality_comment is not UNSET:
            field_dict["allCauseMortalityComment"] = all_cause_mortality_comment
        if event_groups is not UNSET:
            field_dict["eventGroups"] = event_groups
        if serious_events is not UNSET:
            field_dict["seriousEvents"] = serious_events
        if other_events is not UNSET:
            field_dict["otherEvents"] = other_events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adverse_event import AdverseEvent
        from ..models.event_group import EventGroup

        d = src_dict.copy()
        frequency_threshold = d.pop("frequencyThreshold", UNSET)

        time_frame = d.pop("timeFrame", UNSET)

        description = d.pop("description", UNSET)

        all_cause_mortality_comment = d.pop("allCauseMortalityComment", UNSET)

        event_groups = []
        _event_groups = d.pop("eventGroups", UNSET)
        for event_groups_item_data in _event_groups or []:
            event_groups_item = EventGroup.from_dict(event_groups_item_data)

            event_groups.append(event_groups_item)

        serious_events = []
        _serious_events = d.pop("seriousEvents", UNSET)
        for serious_events_item_data in _serious_events or []:
            serious_events_item = AdverseEvent.from_dict(serious_events_item_data)

            serious_events.append(serious_events_item)

        other_events = []
        _other_events = d.pop("otherEvents", UNSET)
        for other_events_item_data in _other_events or []:
            other_events_item = AdverseEvent.from_dict(other_events_item_data)

            other_events.append(other_events_item)

        adverse_events_module = cls(
            frequency_threshold=frequency_threshold,
            time_frame=time_frame,
            description=description,
            all_cause_mortality_comment=all_cause_mortality_comment,
            event_groups=event_groups,
            serious_events=serious_events,
            other_events=other_events,
        )

        adverse_events_module.additional_properties = d
        return adverse_events_module

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
