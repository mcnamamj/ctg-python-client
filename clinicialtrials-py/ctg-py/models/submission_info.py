import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmissionInfo")


@_attrs_define
class SubmissionInfo:
    """
    Attributes:
        release_date (Union[Unset, datetime.date]):
        unrelease_date (Union[Unset, datetime.date]):
        unrelease_date_unknown (Union[Unset, bool]):
        reset_date (Union[Unset, datetime.date]):
        mcp_release_n (Union[Unset, int]):
    """

    release_date: Union[Unset, datetime.date] = UNSET
    unrelease_date: Union[Unset, datetime.date] = UNSET
    unrelease_date_unknown: Union[Unset, bool] = UNSET
    reset_date: Union[Unset, datetime.date] = UNSET
    mcp_release_n: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        release_date: Union[Unset, str] = UNSET
        if not isinstance(self.release_date, Unset):
            release_date = self.release_date.isoformat()

        unrelease_date: Union[Unset, str] = UNSET
        if not isinstance(self.unrelease_date, Unset):
            unrelease_date = self.unrelease_date.isoformat()

        unrelease_date_unknown = self.unrelease_date_unknown

        reset_date: Union[Unset, str] = UNSET
        if not isinstance(self.reset_date, Unset):
            reset_date = self.reset_date.isoformat()

        mcp_release_n = self.mcp_release_n

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if release_date is not UNSET:
            field_dict["releaseDate"] = release_date
        if unrelease_date is not UNSET:
            field_dict["unreleaseDate"] = unrelease_date
        if unrelease_date_unknown is not UNSET:
            field_dict["unreleaseDateUnknown"] = unrelease_date_unknown
        if reset_date is not UNSET:
            field_dict["resetDate"] = reset_date
        if mcp_release_n is not UNSET:
            field_dict["mcpReleaseN"] = mcp_release_n

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _release_date = d.pop("releaseDate", UNSET)
        release_date: Union[Unset, datetime.date]
        if isinstance(_release_date, Unset):
            release_date = UNSET
        else:
            release_date = isoparse(_release_date).date()

        _unrelease_date = d.pop("unreleaseDate", UNSET)
        unrelease_date: Union[Unset, datetime.date]
        if isinstance(_unrelease_date, Unset):
            unrelease_date = UNSET
        else:
            unrelease_date = isoparse(_unrelease_date).date()

        unrelease_date_unknown = d.pop("unreleaseDateUnknown", UNSET)

        _reset_date = d.pop("resetDate", UNSET)
        reset_date: Union[Unset, datetime.date]
        if isinstance(_reset_date, Unset):
            reset_date = UNSET
        else:
            reset_date = isoparse(_reset_date).date()

        mcp_release_n = d.pop("mcpReleaseN", UNSET)

        submission_info = cls(
            release_date=release_date,
            unrelease_date=unrelease_date,
            unrelease_date_unknown=unrelease_date_unknown,
            reset_date=reset_date,
            mcp_release_n=mcp_release_n,
        )

        submission_info.additional_properties = d
        return submission_info

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
