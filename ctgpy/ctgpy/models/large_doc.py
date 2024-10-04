import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LargeDoc")


@_attrs_define
class LargeDoc:
    """
    Attributes:
        type_abbrev (Union[Unset, str]):
        has_protocol (Union[Unset, bool]):
        has_sap (Union[Unset, bool]):
        has_icf (Union[Unset, bool]):
        label (Union[Unset, str]):
        date (Union[Unset, datetime.date]):
        upload_date (Union[Unset, str]): Date and time in `yyyy-MM-dd'T'HH:mm` format
        filename (Union[Unset, str]):
        size (Union[Unset, int]):
    """

    type_abbrev: Union[Unset, str] = UNSET
    has_protocol: Union[Unset, bool] = UNSET
    has_sap: Union[Unset, bool] = UNSET
    has_icf: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    upload_date: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type_abbrev = self.type_abbrev

        has_protocol = self.has_protocol

        has_sap = self.has_sap

        has_icf = self.has_icf

        label = self.label

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        upload_date = self.upload_date

        filename = self.filename

        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_abbrev is not UNSET:
            field_dict["typeAbbrev"] = type_abbrev
        if has_protocol is not UNSET:
            field_dict["hasProtocol"] = has_protocol
        if has_sap is not UNSET:
            field_dict["hasSap"] = has_sap
        if has_icf is not UNSET:
            field_dict["hasIcf"] = has_icf
        if label is not UNSET:
            field_dict["label"] = label
        if date is not UNSET:
            field_dict["date"] = date
        if upload_date is not UNSET:
            field_dict["uploadDate"] = upload_date
        if filename is not UNSET:
            field_dict["filename"] = filename
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type_abbrev = d.pop("typeAbbrev", UNSET)

        has_protocol = d.pop("hasProtocol", UNSET)

        has_sap = d.pop("hasSap", UNSET)

        has_icf = d.pop("hasIcf", UNSET)

        label = d.pop("label", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        upload_date = d.pop("uploadDate", UNSET)

        filename = d.pop("filename", UNSET)

        size = d.pop("size", UNSET)

        large_doc = cls(
            type_abbrev=type_abbrev,
            has_protocol=has_protocol,
            has_sap=has_sap,
            has_icf=has_icf,
            label=label,
            date=date,
            upload_date=upload_date,
            filename=filename,
            size=size,
        )

        large_doc.additional_properties = d
        return large_doc

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
