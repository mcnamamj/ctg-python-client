from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.outcome_measure import OutcomeMeasure


T = TypeVar("T", bound="OutcomeMeasuresModule")


@_attrs_define
class OutcomeMeasuresModule:
    """
    Attributes:
        outcome_measures (Union[Unset, List['OutcomeMeasure']]):
    """

    outcome_measures: Union[Unset, List["OutcomeMeasure"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        outcome_measures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.outcome_measures, Unset):
            outcome_measures = []
            for outcome_measures_item_data in self.outcome_measures:
                outcome_measures_item = outcome_measures_item_data.to_dict()
                outcome_measures.append(outcome_measures_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if outcome_measures is not UNSET:
            field_dict["outcomeMeasures"] = outcome_measures

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.outcome_measure import OutcomeMeasure

        d = src_dict.copy()
        outcome_measures = []
        _outcome_measures = d.pop("outcomeMeasures", UNSET)
        for outcome_measures_item_data in _outcome_measures or []:
            outcome_measures_item = OutcomeMeasure.from_dict(outcome_measures_item_data)

            outcome_measures.append(outcome_measures_item)

        outcome_measures_module = cls(
            outcome_measures=outcome_measures,
        )

        outcome_measures_module.additional_properties = d
        return outcome_measures_module

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
