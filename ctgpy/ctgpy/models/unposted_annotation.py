from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unposted_event import UnpostedEvent


T = TypeVar("T", bound="UnpostedAnnotation")


@_attrs_define
class UnpostedAnnotation:
    """
    Attributes:
        unposted_responsible_party (Union[Unset, str]):
        unposted_events (Union[Unset, List['UnpostedEvent']]):
    """

    unposted_responsible_party: Union[Unset, str] = UNSET
    unposted_events: Union[Unset, List["UnpostedEvent"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unposted_responsible_party = self.unposted_responsible_party

        unposted_events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unposted_events, Unset):
            unposted_events = []
            for unposted_events_item_data in self.unposted_events:
                unposted_events_item = unposted_events_item_data.to_dict()
                unposted_events.append(unposted_events_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unposted_responsible_party is not UNSET:
            field_dict["unpostedResponsibleParty"] = unposted_responsible_party
        if unposted_events is not UNSET:
            field_dict["unpostedEvents"] = unposted_events

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.unposted_event import UnpostedEvent

        d = src_dict.copy()
        unposted_responsible_party = d.pop("unpostedResponsibleParty", UNSET)

        unposted_events = []
        _unposted_events = d.pop("unpostedEvents", UNSET)
        for unposted_events_item_data in _unposted_events or []:
            unposted_events_item = UnpostedEvent.from_dict(unposted_events_item_data)

            unposted_events.append(unposted_events_item)

        unposted_annotation = cls(
            unposted_responsible_party=unposted_responsible_party,
            unposted_events=unposted_events,
        )

        unposted_annotation.additional_properties = d
        return unposted_annotation

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
