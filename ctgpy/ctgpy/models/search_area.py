from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_part import SearchPart


T = TypeVar("T", bound="SearchArea")


@_attrs_define
class SearchArea:
    """
    Attributes:
        name (str):
        parts (List['SearchPart']):
        param (Union[Unset, str]):
        ui_label (Union[Unset, str]):
    """

    name: str
    parts: List["SearchPart"]
    param: Union[Unset, str] = UNSET
    ui_label: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        parts = []
        for parts_item_data in self.parts:
            parts_item = parts_item_data.to_dict()
            parts.append(parts_item)

        param = self.param

        ui_label = self.ui_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
                "parts": parts,
            }
        )
        if param is not UNSET:
            field_dict["param"] = param
        if ui_label is not UNSET:
            field_dict["uiLabel"] = ui_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.search_part import SearchPart

        d = src_dict.copy()
        name = d.pop("name")

        parts = []
        _parts = d.pop("parts")
        for parts_item_data in _parts:
            parts_item = SearchPart.from_dict(parts_item_data)

            parts.append(parts_item)

        param = d.pop("param", UNSET)

        ui_label = d.pop("uiLabel", UNSET)

        search_area = cls(
            name=name,
            parts=parts,
            param=param,
            ui_label=ui_label,
        )

        return search_area
