from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_struct import DateStruct


T = TypeVar("T", bound="FirstMcpInfo")


@_attrs_define
class FirstMcpInfo:
    """
    Attributes:
        post_date_struct (Union[Unset, DateStruct]):
    """

    post_date_struct: Union[Unset, "DateStruct"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        post_date_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.post_date_struct, Unset):
            post_date_struct = self.post_date_struct.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_date_struct is not UNSET:
            field_dict["postDateStruct"] = post_date_struct

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_struct import DateStruct

        d = src_dict.copy()
        _post_date_struct = d.pop("postDateStruct", UNSET)
        post_date_struct: Union[Unset, DateStruct]
        if isinstance(_post_date_struct, Unset):
            post_date_struct = UNSET
        else:
            post_date_struct = DateStruct.from_dict(_post_date_struct)

        first_mcp_info = cls(
            post_date_struct=post_date_struct,
        )

        first_mcp_info.additional_properties = d
        return first_mcp_info

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
