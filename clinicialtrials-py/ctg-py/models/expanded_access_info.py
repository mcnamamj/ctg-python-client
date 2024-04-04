from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.expanded_access_status import ExpandedAccessStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpandedAccessInfo")


@_attrs_define
class ExpandedAccessInfo:
    """
    Attributes:
        has_expanded_access (Union[Unset, bool]):
        nct_id (Union[Unset, str]):
        status_for_nct_id (Union[Unset, ExpandedAccessStatus]):
    """

    has_expanded_access: Union[Unset, bool] = UNSET
    nct_id: Union[Unset, str] = UNSET
    status_for_nct_id: Union[Unset, ExpandedAccessStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_expanded_access = self.has_expanded_access

        nct_id = self.nct_id

        status_for_nct_id: Union[Unset, str] = UNSET
        if not isinstance(self.status_for_nct_id, Unset):
            status_for_nct_id = self.status_for_nct_id.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_expanded_access is not UNSET:
            field_dict["hasExpandedAccess"] = has_expanded_access
        if nct_id is not UNSET:
            field_dict["nctId"] = nct_id
        if status_for_nct_id is not UNSET:
            field_dict["statusForNctId"] = status_for_nct_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        has_expanded_access = d.pop("hasExpandedAccess", UNSET)

        nct_id = d.pop("nctId", UNSET)

        _status_for_nct_id = d.pop("statusForNctId", UNSET)
        status_for_nct_id: Union[Unset, ExpandedAccessStatus]
        if isinstance(_status_for_nct_id, Unset):
            status_for_nct_id = UNSET
        else:
            status_for_nct_id = ExpandedAccessStatus(_status_for_nct_id)

        expanded_access_info = cls(
            has_expanded_access=has_expanded_access,
            nct_id=nct_id,
            status_for_nct_id=status_for_nct_id,
        )

        expanded_access_info.additional_properties = d
        return expanded_access_info

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
