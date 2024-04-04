from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bio_spec_retention import BioSpecRetention
from ..types import UNSET, Unset

T = TypeVar("T", bound="BioSpec")


@_attrs_define
class BioSpec:
    """
    Attributes:
        retention (Union[Unset, BioSpecRetention]):
        description (Union[Unset, str]):
    """

    retention: Union[Unset, BioSpecRetention] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        retention: Union[Unset, str] = UNSET
        if not isinstance(self.retention, Unset):
            retention = self.retention.value

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retention is not UNSET:
            field_dict["retention"] = retention
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _retention = d.pop("retention", UNSET)
        retention: Union[Unset, BioSpecRetention]
        if isinstance(_retention, Unset):
            retention = UNSET
        else:
            retention = BioSpecRetention(_retention)

        description = d.pop("description", UNSET)

        bio_spec = cls(
            retention=retention,
            description=description,
        )

        bio_spec.additional_properties = d
        return bio_spec

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
