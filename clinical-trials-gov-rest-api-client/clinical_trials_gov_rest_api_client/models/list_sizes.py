from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_size import ListSize


T = TypeVar("T", bound="ListSizes")


@_attrs_define
class ListSizes:
    """
    Attributes:
        field (str):
        piece (str):
        unique_sizes_count (int):
        max_size (Union[Unset, int]):
        min_size (Union[Unset, int]):
        top_sizes (Union[Unset, List['ListSize']]):
    """

    field: str
    piece: str
    unique_sizes_count: int
    max_size: Union[Unset, int] = UNSET
    min_size: Union[Unset, int] = UNSET
    top_sizes: Union[Unset, List["ListSize"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        field = self.field

        piece = self.piece

        unique_sizes_count = self.unique_sizes_count

        max_size = self.max_size

        min_size = self.min_size

        top_sizes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.top_sizes, Unset):
            top_sizes = []
            for top_sizes_item_data in self.top_sizes:
                top_sizes_item = top_sizes_item_data.to_dict()
                top_sizes.append(top_sizes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "field": field,
                "piece": piece,
                "uniqueSizesCount": unique_sizes_count,
            }
        )
        if max_size is not UNSET:
            field_dict["maxSize"] = max_size
        if min_size is not UNSET:
            field_dict["minSize"] = min_size
        if top_sizes is not UNSET:
            field_dict["topSizes"] = top_sizes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_size import ListSize

        d = src_dict.copy()
        field = d.pop("field")

        piece = d.pop("piece")

        unique_sizes_count = d.pop("uniqueSizesCount")

        max_size = d.pop("maxSize", UNSET)

        min_size = d.pop("minSize", UNSET)

        top_sizes = []
        _top_sizes = d.pop("topSizes", UNSET)
        for top_sizes_item_data in _top_sizes or []:
            top_sizes_item = ListSize.from_dict(top_sizes_item_data)

            top_sizes.append(top_sizes_item)

        list_sizes = cls(
            field=field,
            piece=piece,
            unique_sizes_count=unique_sizes_count,
            max_size=max_size,
            min_size=min_size,
            top_sizes=top_sizes,
        )

        return list_sizes
