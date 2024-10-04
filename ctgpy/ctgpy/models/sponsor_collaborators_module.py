from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.responsible_party import ResponsibleParty
    from ..models.sponsor import Sponsor


T = TypeVar("T", bound="SponsorCollaboratorsModule")


@_attrs_define
class SponsorCollaboratorsModule:
    """
    Attributes:
        responsible_party (Union[Unset, ResponsibleParty]):
        lead_sponsor (Union[Unset, Sponsor]):
        collaborators (Union[Unset, List['Sponsor']]):
    """

    responsible_party: Union[Unset, "ResponsibleParty"] = UNSET
    lead_sponsor: Union[Unset, "Sponsor"] = UNSET
    collaborators: Union[Unset, List["Sponsor"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        responsible_party: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.responsible_party, Unset):
            responsible_party = self.responsible_party.to_dict()

        lead_sponsor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lead_sponsor, Unset):
            lead_sponsor = self.lead_sponsor.to_dict()

        collaborators: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.collaborators, Unset):
            collaborators = []
            for collaborators_item_data in self.collaborators:
                collaborators_item = collaborators_item_data.to_dict()
                collaborators.append(collaborators_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if responsible_party is not UNSET:
            field_dict["responsibleParty"] = responsible_party
        if lead_sponsor is not UNSET:
            field_dict["leadSponsor"] = lead_sponsor
        if collaborators is not UNSET:
            field_dict["collaborators"] = collaborators

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.responsible_party import ResponsibleParty
        from ..models.sponsor import Sponsor

        d = src_dict.copy()
        _responsible_party = d.pop("responsibleParty", UNSET)
        responsible_party: Union[Unset, ResponsibleParty]
        if isinstance(_responsible_party, Unset):
            responsible_party = UNSET
        else:
            responsible_party = ResponsibleParty.from_dict(_responsible_party)

        _lead_sponsor = d.pop("leadSponsor", UNSET)
        lead_sponsor: Union[Unset, Sponsor]
        if isinstance(_lead_sponsor, Unset):
            lead_sponsor = UNSET
        else:
            lead_sponsor = Sponsor.from_dict(_lead_sponsor)

        collaborators = []
        _collaborators = d.pop("collaborators", UNSET)
        for collaborators_item_data in _collaborators or []:
            collaborators_item = Sponsor.from_dict(collaborators_item_data)

            collaborators.append(collaborators_item)

        sponsor_collaborators_module = cls(
            responsible_party=responsible_party,
            lead_sponsor=lead_sponsor,
            collaborators=collaborators,
        )

        sponsor_collaborators_module.additional_properties = d
        return sponsor_collaborators_module

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
