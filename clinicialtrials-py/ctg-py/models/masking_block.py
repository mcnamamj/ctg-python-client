from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.design_masking import DesignMasking
from ..models.who_masked import WhoMasked
from ..types import UNSET, Unset

T = TypeVar("T", bound="MaskingBlock")


@_attrs_define
class MaskingBlock:
    """
    Attributes:
        masking (Union[Unset, DesignMasking]):
        masking_description (Union[Unset, str]):
        who_masked (Union[Unset, List[WhoMasked]]):
    """

    masking: Union[Unset, DesignMasking] = UNSET
    masking_description: Union[Unset, str] = UNSET
    who_masked: Union[Unset, List[WhoMasked]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        masking: Union[Unset, str] = UNSET
        if not isinstance(self.masking, Unset):
            masking = self.masking.value

        masking_description = self.masking_description

        who_masked: Union[Unset, List[str]] = UNSET
        if not isinstance(self.who_masked, Unset):
            who_masked = []
            for who_masked_item_data in self.who_masked:
                who_masked_item = who_masked_item_data.value
                who_masked.append(who_masked_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if masking is not UNSET:
            field_dict["masking"] = masking
        if masking_description is not UNSET:
            field_dict["maskingDescription"] = masking_description
        if who_masked is not UNSET:
            field_dict["whoMasked"] = who_masked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _masking = d.pop("masking", UNSET)
        masking: Union[Unset, DesignMasking]
        if isinstance(_masking, Unset):
            masking = UNSET
        else:
            masking = DesignMasking(_masking)

        masking_description = d.pop("maskingDescription", UNSET)

        who_masked = []
        _who_masked = d.pop("whoMasked", UNSET)
        for who_masked_item_data in _who_masked or []:
            who_masked_item = WhoMasked(who_masked_item_data)

            who_masked.append(who_masked_item)

        masking_block = cls(
            masking=masking,
            masking_description=masking_description,
            who_masked=who_masked,
        )

        masking_block.additional_properties = d
        return masking_block

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
