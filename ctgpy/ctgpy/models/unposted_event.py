import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.unposted_event_type import UnpostedEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UnpostedEvent")


@_attrs_define
class UnpostedEvent:
    """
    Attributes:
        type (Union[Unset, UnpostedEventType]):
        date (Union[Unset, datetime.date]):
        date_unknown (Union[Unset, bool]):
    """

    type: Union[Unset, UnpostedEventType] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    date_unknown: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        date_unknown = self.date_unknown

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if date is not UNSET:
            field_dict["date"] = date
        if date_unknown is not UNSET:
            field_dict["dateUnknown"] = date_unknown

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, UnpostedEventType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = UnpostedEventType(_type)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        date_unknown = d.pop("dateUnknown", UNSET)

        unposted_event = cls(
            type=type,
            date=date,
            date_unknown=date_unknown,
        )

        unposted_event.additional_properties = d
        return unposted_event

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
