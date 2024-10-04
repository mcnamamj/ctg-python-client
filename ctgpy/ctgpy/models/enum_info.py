from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.enum_item import EnumItem


T = TypeVar("T", bound="EnumInfo")


@_attrs_define
class EnumInfo:
    """
    Attributes:
        pieces (List[str]):
        type (str):
        values (List['EnumItem']):
    """

    pieces: List[str]
    type: str
    values: List["EnumItem"]

    def to_dict(self) -> Dict[str, Any]:
        pieces = self.pieces

        type = self.type

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "pieces": pieces,
                "type": type,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enum_item import EnumItem

        d = src_dict.copy()
        pieces = cast(List[str], d.pop("pieces"))

        type = d.pop("type")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = EnumItem.from_dict(values_item_data)

            values.append(values_item)

        enum_info = cls(
            pieces=pieces,
            type=type,
            values=values,
        )

        return enum_info
