from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agreement_restriction_type import AgreementRestrictionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CertainAgreement")


@_attrs_define
class CertainAgreement:
    """
    Attributes:
        pi_sponsor_employee (Union[Unset, bool]):
        restriction_type (Union[Unset, AgreementRestrictionType]):
        restrictive_agreement (Union[Unset, bool]):
        other_details (Union[Unset, str]):
    """

    pi_sponsor_employee: Union[Unset, bool] = UNSET
    restriction_type: Union[Unset, AgreementRestrictionType] = UNSET
    restrictive_agreement: Union[Unset, bool] = UNSET
    other_details: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pi_sponsor_employee = self.pi_sponsor_employee

        restriction_type: Union[Unset, str] = UNSET
        if not isinstance(self.restriction_type, Unset):
            restriction_type = self.restriction_type.value

        restrictive_agreement = self.restrictive_agreement

        other_details = self.other_details

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pi_sponsor_employee is not UNSET:
            field_dict["piSponsorEmployee"] = pi_sponsor_employee
        if restriction_type is not UNSET:
            field_dict["restrictionType"] = restriction_type
        if restrictive_agreement is not UNSET:
            field_dict["restrictiveAgreement"] = restrictive_agreement
        if other_details is not UNSET:
            field_dict["otherDetails"] = other_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pi_sponsor_employee = d.pop("piSponsorEmployee", UNSET)

        _restriction_type = d.pop("restrictionType", UNSET)
        restriction_type: Union[Unset, AgreementRestrictionType]
        if isinstance(_restriction_type, Unset):
            restriction_type = UNSET
        else:
            restriction_type = AgreementRestrictionType(_restriction_type)

        restrictive_agreement = d.pop("restrictiveAgreement", UNSET)

        other_details = d.pop("otherDetails", UNSET)

        certain_agreement = cls(
            pi_sponsor_employee=pi_sponsor_employee,
            restriction_type=restriction_type,
            restrictive_agreement=restrictive_agreement,
            other_details=other_details,
        )

        certain_agreement.additional_properties = d
        return certain_agreement

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
