from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enum_item_exceptions import EnumItemExceptions


T = TypeVar("T", bound="EnumItem")


@_attrs_define
class EnumItem:
    """
    Attributes:
        legacy_value (str):
        value (str):
        exceptions (Union[Unset, EnumItemExceptions]):
    """

    legacy_value: str
    value: str
    exceptions: Union[Unset, "EnumItemExceptions"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        legacy_value = self.legacy_value

        value = self.value

        exceptions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.exceptions, Unset):
            exceptions = self.exceptions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "legacyValue": legacy_value,
                "value": value,
            }
        )
        if exceptions is not UNSET:
            field_dict["exceptions"] = exceptions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enum_item_exceptions import EnumItemExceptions

        d = src_dict.copy()
        legacy_value = d.pop("legacyValue")

        value = d.pop("value")

        _exceptions = d.pop("exceptions", UNSET)
        exceptions: Union[Unset, EnumItemExceptions]
        if isinstance(_exceptions, Unset):
            exceptions = UNSET
        else:
            exceptions = EnumItemExceptions.from_dict(_exceptions)

        enum_item = cls(
            legacy_value=legacy_value,
            value=value,
            exceptions=exceptions,
        )

        return enum_item
