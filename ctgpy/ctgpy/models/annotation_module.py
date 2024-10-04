from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.unposted_annotation import UnpostedAnnotation
    from ..models.violation_annotation import ViolationAnnotation


T = TypeVar("T", bound="AnnotationModule")


@_attrs_define
class AnnotationModule:
    """
    Attributes:
        unposted_annotation (Union[Unset, UnpostedAnnotation]):
        violation_annotation (Union[Unset, ViolationAnnotation]):
    """

    unposted_annotation: Union[Unset, "UnpostedAnnotation"] = UNSET
    violation_annotation: Union[Unset, "ViolationAnnotation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unposted_annotation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.unposted_annotation, Unset):
            unposted_annotation = self.unposted_annotation.to_dict()

        violation_annotation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.violation_annotation, Unset):
            violation_annotation = self.violation_annotation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unposted_annotation is not UNSET:
            field_dict["unpostedAnnotation"] = unposted_annotation
        if violation_annotation is not UNSET:
            field_dict["violationAnnotation"] = violation_annotation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.unposted_annotation import UnpostedAnnotation
        from ..models.violation_annotation import ViolationAnnotation

        d = src_dict.copy()
        _unposted_annotation = d.pop("unpostedAnnotation", UNSET)
        unposted_annotation: Union[Unset, UnpostedAnnotation]
        if isinstance(_unposted_annotation, Unset):
            unposted_annotation = UNSET
        else:
            unposted_annotation = UnpostedAnnotation.from_dict(_unposted_annotation)

        _violation_annotation = d.pop("violationAnnotation", UNSET)
        violation_annotation: Union[Unset, ViolationAnnotation]
        if isinstance(_violation_annotation, Unset):
            violation_annotation = UNSET
        else:
            violation_annotation = ViolationAnnotation.from_dict(_violation_annotation)

        annotation_module = cls(
            unposted_annotation=unposted_annotation,
            violation_annotation=violation_annotation,
        )

        annotation_module.additional_properties = d
        return annotation_module

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
