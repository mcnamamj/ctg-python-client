from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.large_document_module import LargeDocumentModule


T = TypeVar("T", bound="DocumentSection")


@_attrs_define
class DocumentSection:
    """
    Attributes:
        large_document_module (Union[Unset, LargeDocumentModule]):
    """

    large_document_module: Union[Unset, "LargeDocumentModule"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        large_document_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.large_document_module, Unset):
            large_document_module = self.large_document_module.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if large_document_module is not UNSET:
            field_dict["largeDocumentModule"] = large_document_module

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.large_document_module import LargeDocumentModule

        d = src_dict.copy()
        _large_document_module = d.pop("largeDocumentModule", UNSET)
        large_document_module: Union[Unset, LargeDocumentModule]
        if isinstance(_large_document_module, Unset):
            large_document_module = UNSET
        else:
            large_document_module = LargeDocumentModule.from_dict(_large_document_module)

        document_section = cls(
            large_document_module=large_document_module,
        )

        document_section.additional_properties = d
        return document_section

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
