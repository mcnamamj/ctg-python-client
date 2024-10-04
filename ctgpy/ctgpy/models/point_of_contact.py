from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PointOfContact")


@_attrs_define
class PointOfContact:
    """
    Attributes:
        title (Union[Unset, str]):
        organization (Union[Unset, str]):
        email (Union[Unset, str]):
        phone (Union[Unset, str]):
        phone_ext (Union[Unset, str]):
    """

    title: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    phone_ext: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        organization = self.organization

        email = self.email

        phone = self.phone

        phone_ext = self.phone_ext

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if organization is not UNSET:
            field_dict["organization"] = organization
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if phone_ext is not UNSET:
            field_dict["phoneExt"] = phone_ext

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        organization = d.pop("organization", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        phone_ext = d.pop("phoneExt", UNSET)

        point_of_contact = cls(
            title=title,
            organization=organization,
            email=email,
            phone=phone,
            phone_ext=phone_ext,
        )

        point_of_contact.additional_properties = d
        return point_of_contact

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
