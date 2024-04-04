from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.contact_role import ContactRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    """
    Attributes:
        name (Union[Unset, str]):
        role (Union[Unset, ContactRole]):
        phone (Union[Unset, str]):
        phone_ext (Union[Unset, str]):
        email (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    role: Union[Unset, ContactRole] = UNSET
    phone: Union[Unset, str] = UNSET
    phone_ext: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        phone = self.phone

        phone_ext = self.phone_ext

        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role
        if phone is not UNSET:
            field_dict["phone"] = phone
        if phone_ext is not UNSET:
            field_dict["phoneExt"] = phone_ext
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, ContactRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = ContactRole(_role)

        phone = d.pop("phone", UNSET)

        phone_ext = d.pop("phoneExt", UNSET)

        email = d.pop("email", UNSET)

        contact = cls(
            name=name,
            role=role,
            phone=phone,
            phone_ext=phone_ext,
            email=email,
        )

        contact.additional_properties = d
        return contact

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
