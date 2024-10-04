from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Outcome")


@_attrs_define
class Outcome:
    """
    Attributes:
        measure (Union[Unset, str]):
        description (Union[Unset, str]):
        time_frame (Union[Unset, str]):
    """

    measure: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    time_frame: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        measure = self.measure

        description = self.description

        time_frame = self.time_frame

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if measure is not UNSET:
            field_dict["measure"] = measure
        if description is not UNSET:
            field_dict["description"] = description
        if time_frame is not UNSET:
            field_dict["timeFrame"] = time_frame

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        measure = d.pop("measure", UNSET)

        description = d.pop("description", UNSET)

        time_frame = d.pop("timeFrame", UNSET)

        outcome = cls(
            measure=measure,
            description=description,
            time_frame=time_frame,
        )

        outcome.additional_properties = d
        return outcome

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
