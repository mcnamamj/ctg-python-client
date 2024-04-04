import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.submission_tracking import SubmissionTracking


T = TypeVar("T", bound="MiscInfoModule")


@_attrs_define
class MiscInfoModule:
    """
    Attributes:
        version_holder (Union[Unset, datetime.date]):
        removed_countries (Union[Unset, List[str]]):
        submission_tracking (Union[Unset, SubmissionTracking]):
    """

    version_holder: Union[Unset, datetime.date] = UNSET
    removed_countries: Union[Unset, List[str]] = UNSET
    submission_tracking: Union[Unset, "SubmissionTracking"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version_holder: Union[Unset, str] = UNSET
        if not isinstance(self.version_holder, Unset):
            version_holder = self.version_holder.isoformat()

        removed_countries: Union[Unset, List[str]] = UNSET
        if not isinstance(self.removed_countries, Unset):
            removed_countries = self.removed_countries

        submission_tracking: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.submission_tracking, Unset):
            submission_tracking = self.submission_tracking.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version_holder is not UNSET:
            field_dict["versionHolder"] = version_holder
        if removed_countries is not UNSET:
            field_dict["removedCountries"] = removed_countries
        if submission_tracking is not UNSET:
            field_dict["submissionTracking"] = submission_tracking

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.submission_tracking import SubmissionTracking

        d = src_dict.copy()
        _version_holder = d.pop("versionHolder", UNSET)
        version_holder: Union[Unset, datetime.date]
        if isinstance(_version_holder, Unset):
            version_holder = UNSET
        else:
            version_holder = isoparse(_version_holder).date()

        removed_countries = cast(List[str], d.pop("removedCountries", UNSET))

        _submission_tracking = d.pop("submissionTracking", UNSET)
        submission_tracking: Union[Unset, SubmissionTracking]
        if isinstance(_submission_tracking, Unset):
            submission_tracking = UNSET
        else:
            submission_tracking = SubmissionTracking.from_dict(_submission_tracking)

        misc_info_module = cls(
            version_holder=version_holder,
            removed_countries=removed_countries,
            submission_tracking=submission_tracking,
        )

        misc_info_module.additional_properties = d
        return misc_info_module

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
