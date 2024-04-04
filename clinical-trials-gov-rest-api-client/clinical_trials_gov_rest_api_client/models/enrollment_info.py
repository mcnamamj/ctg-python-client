from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enrollment_type import EnrollmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnrollmentInfo")


@_attrs_define
class EnrollmentInfo:
    """
    Attributes:
        count (Union[Unset, int]):
        type (Union[Unset, EnrollmentType]):
    """

    count: Union[Unset, int] = UNSET
    type: Union[Unset, EnrollmentType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EnrollmentType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EnrollmentType(_type)

        enrollment_info = cls(
            count=count,
            type=type,
        )

        enrollment_info.additional_properties = d
        return enrollment_info

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
