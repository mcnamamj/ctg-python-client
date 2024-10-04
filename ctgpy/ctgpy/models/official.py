from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.official_role import OfficialRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="Official")


@_attrs_define
class Official:
    """
    Attributes:
        name (Union[Unset, str]):
        affiliation (Union[Unset, str]):
        role (Union[Unset, OfficialRole]):
    """

    name: Union[Unset, str] = UNSET
    affiliation: Union[Unset, str] = UNSET
    role: Union[Unset, OfficialRole] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        affiliation = self.affiliation

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if affiliation is not UNSET:
            field_dict["affiliation"] = affiliation
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        affiliation = d.pop("affiliation", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, OfficialRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = OfficialRole(_role)

        official = cls(
            name=name,
            affiliation=affiliation,
            role=role,
        )

        official.additional_properties = d
        return official

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
