from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.adverse_events_module import AdverseEventsModule
    from ..models.baseline_characteristics_module import BaselineCharacteristicsModule
    from ..models.more_info_module import MoreInfoModule
    from ..models.outcome_measures_module import OutcomeMeasuresModule
    from ..models.participant_flow_module import ParticipantFlowModule


T = TypeVar("T", bound="ResultsSection")


@_attrs_define
class ResultsSection:
    """
    Attributes:
        participant_flow_module (Union[Unset, ParticipantFlowModule]):
        baseline_characteristics_module (Union[Unset, BaselineCharacteristicsModule]):
        outcome_measures_module (Union[Unset, OutcomeMeasuresModule]):
        adverse_events_module (Union[Unset, AdverseEventsModule]):
        more_info_module (Union[Unset, MoreInfoModule]):
    """

    participant_flow_module: Union[Unset, "ParticipantFlowModule"] = UNSET
    baseline_characteristics_module: Union[Unset, "BaselineCharacteristicsModule"] = UNSET
    outcome_measures_module: Union[Unset, "OutcomeMeasuresModule"] = UNSET
    adverse_events_module: Union[Unset, "AdverseEventsModule"] = UNSET
    more_info_module: Union[Unset, "MoreInfoModule"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        participant_flow_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.participant_flow_module, Unset):
            participant_flow_module = self.participant_flow_module.to_dict()

        baseline_characteristics_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.baseline_characteristics_module, Unset):
            baseline_characteristics_module = self.baseline_characteristics_module.to_dict()

        outcome_measures_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.outcome_measures_module, Unset):
            outcome_measures_module = self.outcome_measures_module.to_dict()

        adverse_events_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.adverse_events_module, Unset):
            adverse_events_module = self.adverse_events_module.to_dict()

        more_info_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.more_info_module, Unset):
            more_info_module = self.more_info_module.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if participant_flow_module is not UNSET:
            field_dict["participantFlowModule"] = participant_flow_module
        if baseline_characteristics_module is not UNSET:
            field_dict["baselineCharacteristicsModule"] = baseline_characteristics_module
        if outcome_measures_module is not UNSET:
            field_dict["outcomeMeasuresModule"] = outcome_measures_module
        if adverse_events_module is not UNSET:
            field_dict["adverseEventsModule"] = adverse_events_module
        if more_info_module is not UNSET:
            field_dict["moreInfoModule"] = more_info_module

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.adverse_events_module import AdverseEventsModule
        from ..models.baseline_characteristics_module import BaselineCharacteristicsModule
        from ..models.more_info_module import MoreInfoModule
        from ..models.outcome_measures_module import OutcomeMeasuresModule
        from ..models.participant_flow_module import ParticipantFlowModule

        d = src_dict.copy()
        _participant_flow_module = d.pop("participantFlowModule", UNSET)
        participant_flow_module: Union[Unset, ParticipantFlowModule]
        if isinstance(_participant_flow_module, Unset):
            participant_flow_module = UNSET
        else:
            participant_flow_module = ParticipantFlowModule.from_dict(_participant_flow_module)

        _baseline_characteristics_module = d.pop("baselineCharacteristicsModule", UNSET)
        baseline_characteristics_module: Union[Unset, BaselineCharacteristicsModule]
        if isinstance(_baseline_characteristics_module, Unset):
            baseline_characteristics_module = UNSET
        else:
            baseline_characteristics_module = BaselineCharacteristicsModule.from_dict(_baseline_characteristics_module)

        _outcome_measures_module = d.pop("outcomeMeasuresModule", UNSET)
        outcome_measures_module: Union[Unset, OutcomeMeasuresModule]
        if isinstance(_outcome_measures_module, Unset):
            outcome_measures_module = UNSET
        else:
            outcome_measures_module = OutcomeMeasuresModule.from_dict(_outcome_measures_module)

        _adverse_events_module = d.pop("adverseEventsModule", UNSET)
        adverse_events_module: Union[Unset, AdverseEventsModule]
        if isinstance(_adverse_events_module, Unset):
            adverse_events_module = UNSET
        else:
            adverse_events_module = AdverseEventsModule.from_dict(_adverse_events_module)

        _more_info_module = d.pop("moreInfoModule", UNSET)
        more_info_module: Union[Unset, MoreInfoModule]
        if isinstance(_more_info_module, Unset):
            more_info_module = UNSET
        else:
            more_info_module = MoreInfoModule.from_dict(_more_info_module)

        results_section = cls(
            participant_flow_module=participant_flow_module,
            baseline_characteristics_module=baseline_characteristics_module,
            outcome_measures_module=outcome_measures_module,
            adverse_events_module=adverse_events_module,
            more_info_module=more_info_module,
        )

        results_section.additional_properties = d
        return results_section

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
