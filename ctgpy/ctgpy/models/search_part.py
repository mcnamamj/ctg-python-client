from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SearchPart")


@_attrs_define
class SearchPart:
    """
    Attributes:
        is_enum (bool):
        is_synonyms (bool):
        pieces (List[str]):
        type (str):
        weight (float):
    """

    is_enum: bool
    is_synonyms: bool
    pieces: List[str]
    type: str
    weight: float

    def to_dict(self) -> Dict[str, Any]:
        is_enum = self.is_enum

        is_synonyms = self.is_synonyms

        pieces = self.pieces

        type = self.type

        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "isEnum": is_enum,
                "isSynonyms": is_synonyms,
                "pieces": pieces,
                "type": type,
                "weight": weight,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_enum = d.pop("isEnum")

        is_synonyms = d.pop("isSynonyms")

        pieces = cast(List[str], d.pop("pieces"))

        type = d.pop("type")

        weight = d.pop("weight")

        search_part = cls(
            is_enum=is_enum,
            is_synonyms=is_synonyms,
            pieces=pieces,
            type=type,
            weight=weight,
        )

        return search_part
