import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.violation_event_type import ViolationEventType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ViolationEvent")


@_attrs_define
class ViolationEvent:
    """
    Attributes:
        type (Union[Unset, ViolationEventType]):
        description (Union[Unset, str]):
        creation_date (Union[Unset, datetime.date]):
        issued_date (Union[Unset, datetime.date]):
        release_date (Union[Unset, datetime.date]):
        posted_date (Union[Unset, datetime.date]):
    """

    type: Union[Unset, ViolationEventType] = UNSET
    description: Union[Unset, str] = UNSET
    creation_date: Union[Unset, datetime.date] = UNSET
    issued_date: Union[Unset, datetime.date] = UNSET
    release_date: Union[Unset, datetime.date] = UNSET
    posted_date: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        description = self.description

        creation_date: Union[Unset, str] = UNSET
        if not isinstance(self.creation_date, Unset):
            creation_date = self.creation_date.isoformat()

        issued_date: Union[Unset, str] = UNSET
        if not isinstance(self.issued_date, Unset):
            issued_date = self.issued_date.isoformat()

        release_date: Union[Unset, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        posted_date: Union[Unset, str] = UNSET
        if not isinstance(self.posted_date, Unset):
            posted_date = self.posted_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if description is not UNSET:
            field_dict["description"] = description
        if creation_date is not UNSET:
            field_dict["creationDate"] = creation_date
        if issued_date is not UNSET:
            field_dict["issuedDate"] = issued_date
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if posted_date is not UNSET:
            field_dict["postedDate"] = posted_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, ViolationEventType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ViolationEventType(_type)

        description = d.pop("description", UNSET)

        _creation_date = d.pop("creationDate", UNSET)
        creation_date: Union[Unset, datetime.date]
        if isinstance(_creation_date, Unset):
            creation_date = UNSET
        else:
            creation_date = isoparse(_creation_date).date()

        _issued_date = d.pop("issuedDate", UNSET)
        issued_date: Union[Unset, datetime.date]
        if isinstance(_issued_date, Unset):
            issued_date = UNSET
        else:
            issued_date = isoparse(_issued_date).date()

        _release_date = d.pop("releaseDate", UNSET)
        release_date: Union[Unset, datetime.date]
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        _posted_date = d.pop("postedDate", UNSET)
        posted_date: Union[Unset, datetime.date]
        if isinstance(_posted_date, Unset):
            posted_date = UNSET
        else:
            posted_date = isoparse(_posted_date).date()

        violation_event = cls(
            type=type,
            description=description,
            creation_date=creation_date,
            issued_date=issued_date,
            release_date=release_date,
            posted_date=posted_date,
        )

        violation_event.additional_properties = d
        return violation_event

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
