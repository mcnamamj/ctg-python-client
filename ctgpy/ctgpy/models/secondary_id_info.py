from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.secondary_id_type import SecondaryIdType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecondaryIdInfo")


@_attrs_define
class SecondaryIdInfo:
    """
    Attributes:
        id (Union[Unset, str]):
        type (Union[Unset, SecondaryIdType]):
        domain (Union[Unset, str]):
        link (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, SecondaryIdType] = UNSET
    domain: Union[Unset, str] = UNSET
    link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        domain = self.domain

        link = self.link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type is not UNSET:
            field_dict["type"] = type
        if domain is not UNSET:
            field_dict["domain"] = domain
        if link is not UNSET:
            field_dict["link"] = link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, SecondaryIdType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = SecondaryIdType(_type)

        domain = d.pop("domain", UNSET)

        link = d.pop("link", UNSET)

        secondary_id_info = cls(
            id=id,
            type=type,
            domain=domain,
            link=link,
        )

        secondary_id_info.additional_properties = d
        return secondary_id_info

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
