from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certain_agreement import CertainAgreement
    from ..models.limitations_and_caveats import LimitationsAndCaveats
    from ..models.point_of_contact import PointOfContact


T = TypeVar("T", bound="MoreInfoModule")


@_attrs_define
class MoreInfoModule:
    """
    Attributes:
        limitations_and_caveats (Union[Unset, LimitationsAndCaveats]):
        certain_agreement (Union[Unset, CertainAgreement]):
        point_of_contact (Union[Unset, PointOfContact]):
    """

    limitations_and_caveats: Union[Unset, "LimitationsAndCaveats"] = UNSET
    certain_agreement: Union[Unset, "CertainAgreement"] = UNSET
    point_of_contact: Union[Unset, "PointOfContact"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        limitations_and_caveats: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.limitations_and_caveats, Unset):
            limitations_and_caveats = self.limitations_and_caveats.to_dict()

        certain_agreement: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.certain_agreement, Unset):
            certain_agreement = self.certain_agreement.to_dict()

        point_of_contact: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.point_of_contact, Unset):
            point_of_contact = self.point_of_contact.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limitations_and_caveats is not UNSET:
            field_dict["limitationsAndCaveats"] = limitations_and_caveats
        if certain_agreement is not UNSET:
            field_dict["certainAgreement"] = certain_agreement
        if point_of_contact is not UNSET:
            field_dict["pointOfContact"] = point_of_contact

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.certain_agreement import CertainAgreement
        from ..models.limitations_and_caveats import LimitationsAndCaveats
        from ..models.point_of_contact import PointOfContact

        d = src_dict.copy()
        _limitations_and_caveats = d.pop("limitationsAndCaveats", UNSET)
        limitations_and_caveats: Union[Unset, LimitationsAndCaveats]
        if isinstance(_limitations_and_caveats, Unset):
            limitations_and_caveats = UNSET
        else:
            limitations_and_caveats = LimitationsAndCaveats.from_dict(_limitations_and_caveats)

        _certain_agreement = d.pop("certainAgreement", UNSET)
        certain_agreement: Union[Unset, CertainAgreement]
        if isinstance(_certain_agreement, Unset):
            certain_agreement = UNSET
        else:
            certain_agreement = CertainAgreement.from_dict(_certain_agreement)

        _point_of_contact = d.pop("pointOfContact", UNSET)
        point_of_contact: Union[Unset, PointOfContact]
        if isinstance(_point_of_contact, Unset):
            point_of_contact = UNSET
        else:
            point_of_contact = PointOfContact.from_dict(_point_of_contact)

        more_info_module = cls(
            limitations_and_caveats=limitations_and_caveats,
            certain_agreement=certain_agreement,
            point_of_contact=point_of_contact,
        )

        more_info_module.additional_properties = d
        return more_info_module

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
