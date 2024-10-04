from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact import Contact
    from ..models.location import Location
    from ..models.official import Official


T = TypeVar("T", bound="ContactsLocationsModule")


@_attrs_define
class ContactsLocationsModule:
    """
    Attributes:
        central_contacts (Union[Unset, List['Contact']]):
        overall_officials (Union[Unset, List['Official']]):
        locations (Union[Unset, List['Location']]):
    """

    central_contacts: Union[Unset, List["Contact"]] = UNSET
    overall_officials: Union[Unset, List["Official"]] = UNSET
    locations: Union[Unset, List["Location"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        central_contacts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.central_contacts, Unset):
            central_contacts = []
            for central_contacts_item_data in self.central_contacts:
                central_contacts_item = central_contacts_item_data.to_dict()
                central_contacts.append(central_contacts_item)

        overall_officials: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.overall_officials, Unset):
            overall_officials = []
            for overall_officials_item_data in self.overall_officials:
                overall_officials_item = overall_officials_item_data.to_dict()
                overall_officials.append(overall_officials_item)

        locations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if central_contacts is not UNSET:
            field_dict["centralContacts"] = central_contacts
        if overall_officials is not UNSET:
            field_dict["overallOfficials"] = overall_officials
        if locations is not UNSET:
            field_dict["locations"] = locations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contact import Contact
        from ..models.location import Location
        from ..models.official import Official

        d = src_dict.copy()
        central_contacts = []
        _central_contacts = d.pop("centralContacts", UNSET)
        for central_contacts_item_data in _central_contacts or []:
            central_contacts_item = Contact.from_dict(central_contacts_item_data)

            central_contacts.append(central_contacts_item)

        overall_officials = []
        _overall_officials = d.pop("overallOfficials", UNSET)
        for overall_officials_item_data in _overall_officials or []:
            overall_officials_item = Official.from_dict(overall_officials_item_data)

            overall_officials.append(overall_officials_item)

        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in _locations or []:
            locations_item = Location.from_dict(locations_item_data)

            locations.append(locations_item)

        contacts_locations_module = cls(
            central_contacts=central_contacts,
            overall_officials=overall_officials,
            locations=locations,
        )

        contacts_locations_module.additional_properties = d
        return contacts_locations_module

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
