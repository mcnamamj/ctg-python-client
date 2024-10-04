from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.responsible_party_type import ResponsiblePartyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponsibleParty")


@_attrs_define
class ResponsibleParty:
    """
    Attributes:
        type (Union[Unset, ResponsiblePartyType]):
        investigator_full_name (Union[Unset, str]):
        investigator_title (Union[Unset, str]):
        investigator_affiliation (Union[Unset, str]):
        old_name_title (Union[Unset, str]):
        old_organization (Union[Unset, str]):
    """

    type: Union[Unset, ResponsiblePartyType] = UNSET
    investigator_full_name: Union[Unset, str] = UNSET
    investigator_title: Union[Unset, str] = UNSET
    investigator_affiliation: Union[Unset, str] = UNSET
    old_name_title: Union[Unset, str] = UNSET
    old_organization: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        investigator_full_name = self.investigator_full_name

        investigator_title = self.investigator_title

        investigator_affiliation = self.investigator_affiliation

        old_name_title = self.old_name_title

        old_organization = self.old_organization

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if investigator_full_name is not UNSET:
            field_dict["investigatorFullName"] = investigator_full_name
        if investigator_title is not UNSET:
            field_dict["investigatorTitle"] = investigator_title
        if investigator_affiliation is not UNSET:
            field_dict["investigatorAffiliation"] = investigator_affiliation
        if old_name_title is not UNSET:
            field_dict["oldNameTitle"] = old_name_title
        if old_organization is not UNSET:
            field_dict["oldOrganization"] = old_organization

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, ResponsiblePartyType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ResponsiblePartyType(_type)

        investigator_full_name = d.pop("investigatorFullName", UNSET)

        investigator_title = d.pop("investigatorTitle", UNSET)

        investigator_affiliation = d.pop("investigatorAffiliation", UNSET)

        old_name_title = d.pop("oldNameTitle", UNSET)

        old_organization = d.pop("oldOrganization", UNSET)

        responsible_party = cls(
            type=type,
            investigator_full_name=investigator_full_name,
            investigator_title=investigator_title,
            investigator_affiliation=investigator_affiliation,
            old_name_title=old_name_title,
            old_organization=old_organization,
        )

        responsible_party.additional_properties = d
        return responsible_party

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
