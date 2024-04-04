from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.large_doc import LargeDoc


T = TypeVar("T", bound="LargeDocumentModule")


@_attrs_define
class LargeDocumentModule:
    """
    Attributes:
        no_sap (Union[Unset, bool]):
        large_docs (Union[Unset, List['LargeDoc']]):
    """

    no_sap: Union[Unset, bool] = UNSET
    large_docs: Union[Unset, List["LargeDoc"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        no_sap = self.no_sap

        large_docs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.large_docs, Unset):
            large_docs = []
            for large_docs_item_data in self.large_docs:
                large_docs_item = large_docs_item_data.to_dict()
                large_docs.append(large_docs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_sap is not UNSET:
            field_dict["noSap"] = no_sap
        if large_docs is not UNSET:
            field_dict["largeDocs"] = large_docs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.large_doc import LargeDoc

        d = src_dict.copy()
        no_sap = d.pop("noSap", UNSET)

        large_docs = []
        _large_docs = d.pop("largeDocs", UNSET)
        for large_docs_item_data in _large_docs or []:
            large_docs_item = LargeDoc.from_dict(large_docs_item_data)

            large_docs.append(large_docs_item)

        large_document_module = cls(
            no_sap=no_sap,
            large_docs=large_docs,
        )

        large_document_module.additional_properties = d
        return large_document_module

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
