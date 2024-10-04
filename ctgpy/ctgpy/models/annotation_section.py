from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_module import AnnotationModule


T = TypeVar("T", bound="AnnotationSection")


@_attrs_define
class AnnotationSection:
    """
    Attributes:
        annotation_module (Union[Unset, AnnotationModule]):
    """

    annotation_module: Union[Unset, "AnnotationModule"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        annotation_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotation_module, Unset):
            annotation_module = self.annotation_module.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if annotation_module is not UNSET:
            field_dict["annotationModule"] = annotation_module

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annotation_module import AnnotationModule

        d = src_dict.copy()
        _annotation_module = d.pop("annotationModule", UNSET)
        annotation_module: Union[Unset, AnnotationModule]
        if isinstance(_annotation_module, Unset):
            annotation_module = UNSET
        else:
            annotation_module = AnnotationModule.from_dict(_annotation_module)

        annotation_section = cls(
            annotation_module=annotation_module,
        )

        annotation_section.additional_properties = d
        return annotation_section

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
