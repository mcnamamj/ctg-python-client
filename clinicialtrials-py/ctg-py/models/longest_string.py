from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="LongestString")


@_attrs_define
class LongestString:
    """
    Attributes:
        length (int):
        nct_id (str):
        value (str):
    """

    length: int
    nct_id: str
    value: str

    def to_dict(self) -> Dict[str, Any]:
        length = self.length

        nct_id = self.nct_id

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "length": length,
                "nctId": nct_id,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        length = d.pop("length")

        nct_id = d.pop("nctId")

        value = d.pop("value")

        longest_string = cls(
            length=length,
            nct_id=nct_id,
            value=value,
        )

        return longest_string
