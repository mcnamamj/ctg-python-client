from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.denom import Denom
    from ..models.measure_category import MeasureCategory


T = TypeVar("T", bound="MeasureClass")


@_attrs_define
class MeasureClass:
    """
    Attributes:
        title (Union[Unset, str]):
        denoms (Union[Unset, List['Denom']]):
        categories (Union[Unset, List['MeasureCategory']]):
    """

    title: Union[Unset, str] = UNSET
    denoms: Union[Unset, List["Denom"]] = UNSET
    categories: Union[Unset, List["MeasureCategory"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        denoms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.denoms, Unset):
            denoms = []
            for denoms_item_data in self.denoms:
                denoms_item = denoms_item_data.to_dict()
                denoms.append(denoms_item)

        categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if denoms is not UNSET:
            field_dict["denoms"] = denoms
        if categories is not UNSET:
            field_dict["categories"] = categories

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.denom import Denom
        from ..models.measure_category import MeasureCategory

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        denoms = []
        _denoms = d.pop("denoms", UNSET)
        for denoms_item_data in _denoms or []:
            denoms_item = Denom.from_dict(denoms_item_data)

            denoms.append(denoms_item)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = MeasureCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        measure_class = cls(
            title=title,
            denoms=denoms,
            categories=categories,
        )

        measure_class.additional_properties = d
        return measure_class

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
