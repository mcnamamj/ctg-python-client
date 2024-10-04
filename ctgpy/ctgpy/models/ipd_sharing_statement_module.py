from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ipd_sharing import IpdSharing
from ..models.ipd_sharing_info_type import IpdSharingInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IpdSharingStatementModule")


@_attrs_define
class IpdSharingStatementModule:
    """
    Attributes:
        ipd_sharing (Union[Unset, IpdSharing]):
        description (Union[Unset, str]):
        info_types (Union[Unset, List[IpdSharingInfoType]]):
        time_frame (Union[Unset, str]):
        access_criteria (Union[Unset, str]):
        url (Union[Unset, str]):
    """

    ipd_sharing: Union[Unset, IpdSharing] = UNSET
    description: Union[Unset, str] = UNSET
    info_types: Union[Unset, List[IpdSharingInfoType]] = UNSET
    time_frame: Union[Unset, str] = UNSET
    access_criteria: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ipd_sharing: Union[Unset, str] = UNSET
        if not isinstance(self.ipd_sharing, Unset):
            ipd_sharing = self.ipd_sharing.value

        description = self.description

        info_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.info_types, Unset):
            info_types = []
            for info_types_item_data in self.info_types:
                info_types_item = info_types_item_data.value
                info_types.append(info_types_item)

        time_frame = self.time_frame

        access_criteria = self.access_criteria

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipd_sharing is not UNSET:
            field_dict["ipdSharing"] = ipd_sharing
        if description is not UNSET:
            field_dict["description"] = description
        if info_types is not UNSET:
            field_dict["infoTypes"] = info_types
        if time_frame is not UNSET:
            field_dict["timeFrame"] = time_frame
        if access_criteria is not UNSET:
            field_dict["accessCriteria"] = access_criteria
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _ipd_sharing = d.pop("ipdSharing", UNSET)
        ipd_sharing: Union[Unset, IpdSharing]
        if isinstance(_ipd_sharing, Unset):
            ipd_sharing = UNSET
        else:
            ipd_sharing = IpdSharing(_ipd_sharing)

        description = d.pop("description", UNSET)

        info_types = []
        _info_types = d.pop("infoTypes", UNSET)
        for info_types_item_data in _info_types or []:
            info_types_item = IpdSharingInfoType(info_types_item_data)

            info_types.append(info_types_item)

        time_frame = d.pop("timeFrame", UNSET)

        access_criteria = d.pop("accessCriteria", UNSET)

        url = d.pop("url", UNSET)

        ipd_sharing_statement_module = cls(
            ipd_sharing=ipd_sharing,
            description=description,
            info_types=info_types,
            time_frame=time_frame,
            access_criteria=access_criteria,
            url=url,
        )

        ipd_sharing_statement_module.additional_properties = d
        return ipd_sharing_statement_module

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
