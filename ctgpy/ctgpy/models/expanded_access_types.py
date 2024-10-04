from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpandedAccessTypes")


@_attrs_define
class ExpandedAccessTypes:
    """
    Attributes:
        individual (Union[Unset, bool]):
        intermediate (Union[Unset, bool]):
        treatment (Union[Unset, bool]):
    """

    individual: Union[Unset, bool] = UNSET
    intermediate: Union[Unset, bool] = UNSET
    treatment: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        individual = self.individual

        intermediate = self.intermediate

        treatment = self.treatment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if individual is not UNSET:
            field_dict["individual"] = individual
        if intermediate is not UNSET:
            field_dict["intermediate"] = intermediate
        if treatment is not UNSET:
            field_dict["treatment"] = treatment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        individual = d.pop("individual", UNSET)

        intermediate = d.pop("intermediate", UNSET)

        treatment = d.pop("treatment", UNSET)

        expanded_access_types = cls(
            individual=individual,
            intermediate=intermediate,
            treatment=treatment,
        )

        expanded_access_types.additional_properties = d
        return expanded_access_types

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
