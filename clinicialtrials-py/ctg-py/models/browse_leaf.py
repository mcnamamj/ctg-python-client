from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.browse_leaf_relevance import BrowseLeafRelevance
from ..types import UNSET, Unset

T = TypeVar("T", bound="BrowseLeaf")


@_attrs_define
class BrowseLeaf:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        as_found (Union[Unset, str]):
        relevance (Union[Unset, BrowseLeafRelevance]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    as_found: Union[Unset, str] = UNSET
    relevance: Union[Unset, BrowseLeafRelevance] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        as_found = self.as_found

        relevance: Union[Unset, str] = UNSET
        if not isinstance(self.relevance, Unset):
            relevance = self.relevance.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if as_found is not UNSET:
            field_dict["asFound"] = as_found
        if relevance is not UNSET:
            field_dict["relevance"] = relevance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        as_found = d.pop("asFound", UNSET)

        _relevance = d.pop("relevance", UNSET)
        relevance: Union[Unset, BrowseLeafRelevance]
        if isinstance(_relevance, Unset):
            relevance = UNSET
        else:
            relevance = BrowseLeafRelevance(_relevance)

        browse_leaf = cls(
            id=id,
            name=name,
            as_found=as_found,
            relevance=relevance,
        )

        browse_leaf.additional_properties = d
        return browse_leaf

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
