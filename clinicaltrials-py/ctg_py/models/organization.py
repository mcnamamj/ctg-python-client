from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agency_class import AgencyClass
from ..types import UNSET, Unset

T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """
    Attributes:
        full_name (Union[Unset, str]):
        class_ (Union[Unset, AgencyClass]):
    """

    full_name: Union[Unset, str] = UNSET
    class_: Union[Unset, AgencyClass] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_name = self.full_name

        class_: Union[Unset, str] = UNSET
        if not isinstance(self.class_, Unset):
            class_ = self.class_.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if class_ is not UNSET:
            field_dict["class"] = class_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        full_name = d.pop("fullName", UNSET)

        _class_ = d.pop("class", UNSET)
        class_: Union[Unset, AgencyClass]
        if isinstance(_class_, Unset):
            class_ = UNSET
        else:
            class_ = AgencyClass(_class_)

        organization = cls(
            full_name=full_name,
            class_=class_,
        )

        organization.additional_properties = d
        return organization

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
