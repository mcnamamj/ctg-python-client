from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_assessment import EventAssessment
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_stats import EventStats


T = TypeVar("T", bound="AdverseEvent")


@_attrs_define
class AdverseEvent:
    """
    Attributes:
        term (Union[Unset, str]):
        organ_system (Union[Unset, str]):
        source_vocabulary (Union[Unset, str]):
        assessment_type (Union[Unset, EventAssessment]):
        notes (Union[Unset, str]):
        stats (Union[Unset, List['EventStats']]):
    """

    term: Union[Unset, str] = UNSET
    organ_system: Union[Unset, str] = UNSET
    source_vocabulary: Union[Unset, str] = UNSET
    assessment_type: Union[Unset, EventAssessment] = UNSET
    notes: Union[Unset, str] = UNSET
    stats: Union[Unset, List["EventStats"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        term = self.term

        organ_system = self.organ_system

        source_vocabulary = self.source_vocabulary

        assessment_type: Union[Unset, str] = UNSET
        if not isinstance(self.assessment_type, Unset):
            assessment_type = self.assessment_type.value

        notes = self.notes

        stats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if organ_system is not UNSET:
            field_dict["organSystem"] = organ_system
        if source_vocabulary is not UNSET:
            field_dict["sourceVocabulary"] = source_vocabulary
        if assessment_type is not UNSET:
            field_dict["assessmentType"] = assessment_type
        if notes is not UNSET:
            field_dict["notes"] = notes
        if stats is not UNSET:
            field_dict["stats"] = stats

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.event_stats import EventStats

        d = src_dict.copy()
        term = d.pop("term", UNSET)

        organ_system = d.pop("organSystem", UNSET)

        source_vocabulary = d.pop("sourceVocabulary", UNSET)

        _assessment_type = d.pop("assessmentType", UNSET)
        assessment_type: Union[Unset, EventAssessment]
        if isinstance(_assessment_type, Unset):
            assessment_type = UNSET
        else:
            assessment_type = EventAssessment(_assessment_type)

        notes = d.pop("notes", UNSET)

        stats = []
        _stats = d.pop("stats", UNSET)
        for stats_item_data in _stats or []:
            stats_item = EventStats.from_dict(stats_item_data)

            stats.append(stats_item)

        adverse_event = cls(
            term=term,
            organ_system=organ_system,
            source_vocabulary=source_vocabulary,
            assessment_type=assessment_type,
            notes=notes,
            stats=stats,
        )

        adverse_event.additional_properties = d
        return adverse_event

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
