from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation_section import AnnotationSection
    from ..models.derived_section import DerivedSection
    from ..models.document_section import DocumentSection
    from ..models.protocol_section import ProtocolSection
    from ..models.results_section import ResultsSection


T = TypeVar("T", bound="Study")


@_attrs_define
class Study:
    """
    Attributes:
        protocol_section (Union[Unset, ProtocolSection]):
        results_section (Union[Unset, ResultsSection]):
        annotation_section (Union[Unset, AnnotationSection]):
        document_section (Union[Unset, DocumentSection]):
        derived_section (Union[Unset, DerivedSection]):
        has_results (Union[Unset, bool]):
    """

    protocol_section: Union[Unset, "ProtocolSection"] = UNSET
    results_section: Union[Unset, "ResultsSection"] = UNSET
    annotation_section: Union[Unset, "AnnotationSection"] = UNSET
    document_section: Union[Unset, "DocumentSection"] = UNSET
    derived_section: Union[Unset, "DerivedSection"] = UNSET
    has_results: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol_section: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.protocol_section, Unset):
            protocol_section = self.protocol_section.to_dict()

        results_section: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.results_section, Unset):
            results_section = self.results_section.to_dict()

        annotation_section: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.annotation_section, Unset):
            annotation_section = self.annotation_section.to_dict()

        document_section: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.document_section, Unset):
            document_section = self.document_section.to_dict()

        derived_section: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.derived_section, Unset):
            derived_section = self.derived_section.to_dict()

        has_results = self.has_results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if protocol_section is not UNSET:
            field_dict["protocolSection"] = protocol_section
        if results_section is not UNSET:
            field_dict["resultsSection"] = results_section
        if annotation_section is not UNSET:
            field_dict["annotationSection"] = annotation_section
        if document_section is not UNSET:
            field_dict["documentSection"] = document_section
        if derived_section is not UNSET:
            field_dict["derivedSection"] = derived_section
        if has_results is not UNSET:
            field_dict["hasResults"] = has_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annotation_section import AnnotationSection
        from ..models.derived_section import DerivedSection
        from ..models.document_section import DocumentSection
        from ..models.protocol_section import ProtocolSection
        from ..models.results_section import ResultsSection

        d = src_dict.copy()
        _protocol_section = d.pop("protocolSection", UNSET)
        protocol_section: Union[Unset, ProtocolSection]
        if isinstance(_protocol_section, Unset):
            protocol_section = UNSET
        else:
            protocol_section = ProtocolSection.from_dict(_protocol_section)

        _results_section = d.pop("resultsSection", UNSET)
        results_section: Union[Unset, ResultsSection]
        if isinstance(_results_section, Unset):
            results_section = UNSET
        else:
            results_section = ResultsSection.from_dict(_results_section)

        _annotation_section = d.pop("annotationSection", UNSET)
        annotation_section: Union[Unset, AnnotationSection]
        if isinstance(_annotation_section, Unset):
            annotation_section = UNSET
        else:
            annotation_section = AnnotationSection.from_dict(_annotation_section)

        _document_section = d.pop("documentSection", UNSET)
        document_section: Union[Unset, DocumentSection]
        if isinstance(_document_section, Unset):
            document_section = UNSET
        else:
            document_section = DocumentSection.from_dict(_document_section)

        _derived_section = d.pop("derivedSection", UNSET)
        derived_section: Union[Unset, DerivedSection]
        if isinstance(_derived_section, Unset):
            derived_section = UNSET
        else:
            derived_section = DerivedSection.from_dict(_derived_section)

        has_results = d.pop("hasResults", UNSET)

        study = cls(
            protocol_section=protocol_section,
            results_section=results_section,
            annotation_section=annotation_section,
            document_section=document_section,
            derived_section=derived_section,
            has_results=has_results,
        )

        study.additional_properties = d
        return study

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
