from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.arms_interventions_module import ArmsInterventionsModule
    from ..models.conditions_module import ConditionsModule
    from ..models.contacts_locations_module import ContactsLocationsModule
    from ..models.description_module import DescriptionModule
    from ..models.design_module import DesignModule
    from ..models.eligibility_module import EligibilityModule
    from ..models.identification_module import IdentificationModule
    from ..models.ipd_sharing_statement_module import IpdSharingStatementModule
    from ..models.outcomes_module import OutcomesModule
    from ..models.oversight_module import OversightModule
    from ..models.references_module import ReferencesModule
    from ..models.sponsor_collaborators_module import SponsorCollaboratorsModule
    from ..models.status_module import StatusModule


T = TypeVar("T", bound="ProtocolSection")


@_attrs_define
class ProtocolSection:
    """
    Attributes:
        identification_module (Union[Unset, IdentificationModule]):
        status_module (Union[Unset, StatusModule]):
        sponsor_collaborators_module (Union[Unset, SponsorCollaboratorsModule]):
        oversight_module (Union[Unset, OversightModule]):
        description_module (Union[Unset, DescriptionModule]):
        conditions_module (Union[Unset, ConditionsModule]):
        design_module (Union[Unset, DesignModule]):
        arms_interventions_module (Union[Unset, ArmsInterventionsModule]):
        outcomes_module (Union[Unset, OutcomesModule]):
        eligibility_module (Union[Unset, EligibilityModule]):
        contacts_locations_module (Union[Unset, ContactsLocationsModule]):
        references_module (Union[Unset, ReferencesModule]):
        ipd_sharing_statement_module (Union[Unset, IpdSharingStatementModule]):
    """

    identification_module: Union[Unset, "IdentificationModule"] = UNSET
    status_module: Union[Unset, "StatusModule"] = UNSET
    sponsor_collaborators_module: Union[Unset, "SponsorCollaboratorsModule"] = UNSET
    oversight_module: Union[Unset, "OversightModule"] = UNSET
    description_module: Union[Unset, "DescriptionModule"] = UNSET
    conditions_module: Union[Unset, "ConditionsModule"] = UNSET
    design_module: Union[Unset, "DesignModule"] = UNSET
    arms_interventions_module: Union[Unset, "ArmsInterventionsModule"] = UNSET
    outcomes_module: Union[Unset, "OutcomesModule"] = UNSET
    eligibility_module: Union[Unset, "EligibilityModule"] = UNSET
    contacts_locations_module: Union[Unset, "ContactsLocationsModule"] = UNSET
    references_module: Union[Unset, "ReferencesModule"] = UNSET
    ipd_sharing_statement_module: Union[Unset, "IpdSharingStatementModule"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identification_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identification_module, Unset):
            identification_module = self.identification_module.to_dict()

        status_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.status_module, Unset):
            status_module = self.status_module.to_dict()

        sponsor_collaborators_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sponsor_collaborators_module, Unset):
            sponsor_collaborators_module = self.sponsor_collaborators_module.to_dict()

        oversight_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oversight_module, Unset):
            oversight_module = self.oversight_module.to_dict()

        description_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.description_module, Unset):
            description_module = self.description_module.to_dict()

        conditions_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conditions_module, Unset):
            conditions_module = self.conditions_module.to_dict()

        design_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.design_module, Unset):
            design_module = self.design_module.to_dict()

        arms_interventions_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arms_interventions_module, Unset):
            arms_interventions_module = self.arms_interventions_module.to_dict()

        outcomes_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.outcomes_module, Unset):
            outcomes_module = self.outcomes_module.to_dict()

        eligibility_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.eligibility_module, Unset):
            eligibility_module = self.eligibility_module.to_dict()

        contacts_locations_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contacts_locations_module, Unset):
            contacts_locations_module = self.contacts_locations_module.to_dict()

        references_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.references_module, Unset):
            references_module = self.references_module.to_dict()

        ipd_sharing_statement_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ipd_sharing_statement_module, Unset):
            ipd_sharing_statement_module = self.ipd_sharing_statement_module.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identification_module is not UNSET:
            field_dict["identificationModule"] = identification_module
        if status_module is not UNSET:
            field_dict["statusModule"] = status_module
        if sponsor_collaborators_module is not UNSET:
            field_dict["sponsorCollaboratorsModule"] = sponsor_collaborators_module
        if oversight_module is not UNSET:
            field_dict["oversightModule"] = oversight_module
        if description_module is not UNSET:
            field_dict["descriptionModule"] = description_module
        if conditions_module is not UNSET:
            field_dict["conditionsModule"] = conditions_module
        if design_module is not UNSET:
            field_dict["designModule"] = design_module
        if arms_interventions_module is not UNSET:
            field_dict["armsInterventionsModule"] = arms_interventions_module
        if outcomes_module is not UNSET:
            field_dict["outcomesModule"] = outcomes_module
        if eligibility_module is not UNSET:
            field_dict["eligibilityModule"] = eligibility_module
        if contacts_locations_module is not UNSET:
            field_dict["contactsLocationsModule"] = contacts_locations_module
        if references_module is not UNSET:
            field_dict["referencesModule"] = references_module
        if ipd_sharing_statement_module is not UNSET:
            field_dict["ipdSharingStatementModule"] = ipd_sharing_statement_module

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.arms_interventions_module import ArmsInterventionsModule
        from ..models.conditions_module import ConditionsModule
        from ..models.contacts_locations_module import ContactsLocationsModule
        from ..models.description_module import DescriptionModule
        from ..models.design_module import DesignModule
        from ..models.eligibility_module import EligibilityModule
        from ..models.identification_module import IdentificationModule
        from ..models.ipd_sharing_statement_module import IpdSharingStatementModule
        from ..models.outcomes_module import OutcomesModule
        from ..models.oversight_module import OversightModule
        from ..models.references_module import ReferencesModule
        from ..models.sponsor_collaborators_module import SponsorCollaboratorsModule
        from ..models.status_module import StatusModule

        d = src_dict.copy()
        _identification_module = d.pop("identificationModule", UNSET)
        identification_module: Union[Unset, IdentificationModule]
        if isinstance(_identification_module, Unset):
            identification_module = UNSET
        else:
            identification_module = IdentificationModule.from_dict(_identification_module)

        _status_module = d.pop("statusModule", UNSET)
        status_module: Union[Unset, StatusModule]
        if isinstance(_status_module, Unset):
            status_module = UNSET
        else:
            status_module = StatusModule.from_dict(_status_module)

        _sponsor_collaborators_module = d.pop("sponsorCollaboratorsModule", UNSET)
        sponsor_collaborators_module: Union[Unset, SponsorCollaboratorsModule]
        if isinstance(_sponsor_collaborators_module, Unset):
            sponsor_collaborators_module = UNSET
        else:
            sponsor_collaborators_module = SponsorCollaboratorsModule.from_dict(_sponsor_collaborators_module)

        _oversight_module = d.pop("oversightModule", UNSET)
        oversight_module: Union[Unset, OversightModule]
        if isinstance(_oversight_module, Unset):
            oversight_module = UNSET
        else:
            oversight_module = OversightModule.from_dict(_oversight_module)

        _description_module = d.pop("descriptionModule", UNSET)
        description_module: Union[Unset, DescriptionModule]
        if isinstance(_description_module, Unset):
            description_module = UNSET
        else:
            description_module = DescriptionModule.from_dict(_description_module)

        _conditions_module = d.pop("conditionsModule", UNSET)
        conditions_module: Union[Unset, ConditionsModule]
        if isinstance(_conditions_module, Unset):
            conditions_module = UNSET
        else:
            conditions_module = ConditionsModule.from_dict(_conditions_module)

        _design_module = d.pop("designModule", UNSET)
        design_module: Union[Unset, DesignModule]
        if isinstance(_design_module, Unset):
            design_module = UNSET
        else:
            design_module = DesignModule.from_dict(_design_module)

        _arms_interventions_module = d.pop("armsInterventionsModule", UNSET)
        arms_interventions_module: Union[Unset, ArmsInterventionsModule]
        if isinstance(_arms_interventions_module, Unset):
            arms_interventions_module = UNSET
        else:
            arms_interventions_module = ArmsInterventionsModule.from_dict(_arms_interventions_module)

        _outcomes_module = d.pop("outcomesModule", UNSET)
        outcomes_module: Union[Unset, OutcomesModule]
        if isinstance(_outcomes_module, Unset):
            outcomes_module = UNSET
        else:
            outcomes_module = OutcomesModule.from_dict(_outcomes_module)

        _eligibility_module = d.pop("eligibilityModule", UNSET)
        eligibility_module: Union[Unset, EligibilityModule]
        if isinstance(_eligibility_module, Unset):
            eligibility_module = UNSET
        else:
            eligibility_module = EligibilityModule.from_dict(_eligibility_module)

        _contacts_locations_module = d.pop("contactsLocationsModule", UNSET)
        contacts_locations_module: Union[Unset, ContactsLocationsModule]
        if isinstance(_contacts_locations_module, Unset):
            contacts_locations_module = UNSET
        else:
            contacts_locations_module = ContactsLocationsModule.from_dict(_contacts_locations_module)

        _references_module = d.pop("referencesModule", UNSET)
        references_module: Union[Unset, ReferencesModule]
        if isinstance(_references_module, Unset):
            references_module = UNSET
        else:
            references_module = ReferencesModule.from_dict(_references_module)

        _ipd_sharing_statement_module = d.pop("ipdSharingStatementModule", UNSET)
        ipd_sharing_statement_module: Union[Unset, IpdSharingStatementModule]
        if isinstance(_ipd_sharing_statement_module, Unset):
            ipd_sharing_statement_module = UNSET
        else:
            ipd_sharing_statement_module = IpdSharingStatementModule.from_dict(_ipd_sharing_statement_module)

        protocol_section = cls(
            identification_module=identification_module,
            status_module=status_module,
            sponsor_collaborators_module=sponsor_collaborators_module,
            oversight_module=oversight_module,
            description_module=description_module,
            conditions_module=conditions_module,
            design_module=design_module,
            arms_interventions_module=arms_interventions_module,
            outcomes_module=outcomes_module,
            eligibility_module=eligibility_module,
            contacts_locations_module=contacts_locations_module,
            references_module=references_module,
            ipd_sharing_statement_module=ipd_sharing_statement_module,
        )

        protocol_section.additional_properties = d
        return protocol_section

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
