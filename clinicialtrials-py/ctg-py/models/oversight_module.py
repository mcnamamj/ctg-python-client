from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OversightModule")


@_attrs_define
class OversightModule:
    """
    Attributes:
        oversight_has_dmc (Union[Unset, bool]):
        is_fda_regulated_drug (Union[Unset, bool]):
        is_fda_regulated_device (Union[Unset, bool]):
        is_unapproved_device (Union[Unset, bool]):
        is_ppsd (Union[Unset, bool]):
        is_us_export (Union[Unset, bool]):
        fdaaa_801_violation (Union[Unset, bool]):
    """

    oversight_has_dmc: Union[Unset, bool] = UNSET
    is_fda_regulated_drug: Union[Unset, bool] = UNSET
    is_fda_regulated_device: Union[Unset, bool] = UNSET
    is_unapproved_device: Union[Unset, bool] = UNSET
    is_ppsd: Union[Unset, bool] = UNSET
    is_us_export: Union[Unset, bool] = UNSET
    fdaaa_801_violation: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        oversight_has_dmc = self.oversight_has_dmc

        is_fda_regulated_drug = self.is_fda_regulated_drug

        is_fda_regulated_device = self.is_fda_regulated_device

        is_unapproved_device = self.is_unapproved_device

        is_ppsd = self.is_ppsd

        is_us_export = self.is_us_export

        fdaaa_801_violation = self.fdaaa_801_violation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oversight_has_dmc is not UNSET:
            field_dict["oversightHasDmc"] = oversight_has_dmc
        if is_fda_regulated_drug is not UNSET:
            field_dict["isFdaRegulatedDrug"] = is_fda_regulated_drug
        if is_fda_regulated_device is not UNSET:
            field_dict["isFdaRegulatedDevice"] = is_fda_regulated_device
        if is_unapproved_device is not UNSET:
            field_dict["isUnapprovedDevice"] = is_unapproved_device
        if is_ppsd is not UNSET:
            field_dict["isPpsd"] = is_ppsd
        if is_us_export is not UNSET:
            field_dict["isUsExport"] = is_us_export
        if fdaaa_801_violation is not UNSET:
            field_dict["fdaaa801Violation"] = fdaaa_801_violation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        oversight_has_dmc = d.pop("oversightHasDmc", UNSET)

        is_fda_regulated_drug = d.pop("isFdaRegulatedDrug", UNSET)

        is_fda_regulated_device = d.pop("isFdaRegulatedDevice", UNSET)

        is_unapproved_device = d.pop("isUnapprovedDevice", UNSET)

        is_ppsd = d.pop("isPpsd", UNSET)

        is_us_export = d.pop("isUsExport", UNSET)

        fdaaa_801_violation = d.pop("fdaaa801Violation", UNSET)

        oversight_module = cls(
            oversight_has_dmc=oversight_has_dmc,
            is_fda_regulated_drug=is_fda_regulated_drug,
            is_fda_regulated_device=is_fda_regulated_device,
            is_unapproved_device=is_unapproved_device,
            is_ppsd=is_ppsd,
            is_us_export=is_us_export,
            fdaaa_801_violation=fdaaa_801_violation,
        )

        oversight_module.additional_properties = d
        return oversight_module

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
