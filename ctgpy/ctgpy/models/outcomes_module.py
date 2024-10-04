from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.outcome import Outcome


T = TypeVar("T", bound="OutcomesModule")


@_attrs_define
class OutcomesModule:
    """
    Attributes:
        primary_outcomes (Union[Unset, List['Outcome']]):
        secondary_outcomes (Union[Unset, List['Outcome']]):
        other_outcomes (Union[Unset, List['Outcome']]):
    """

    primary_outcomes: Union[Unset, List["Outcome"]] = UNSET
    secondary_outcomes: Union[Unset, List["Outcome"]] = UNSET
    other_outcomes: Union[Unset, List["Outcome"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        primary_outcomes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.primary_outcomes, Unset):
            primary_outcomes = []
            for primary_outcomes_item_data in self.primary_outcomes:
                primary_outcomes_item = primary_outcomes_item_data.to_dict()
                primary_outcomes.append(primary_outcomes_item)

        secondary_outcomes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.secondary_outcomes, Unset):
            secondary_outcomes = []
            for secondary_outcomes_item_data in self.secondary_outcomes:
                secondary_outcomes_item = secondary_outcomes_item_data.to_dict()
                secondary_outcomes.append(secondary_outcomes_item)

        other_outcomes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.other_outcomes, Unset):
            other_outcomes = []
            for other_outcomes_item_data in self.other_outcomes:
                other_outcomes_item = other_outcomes_item_data.to_dict()
                other_outcomes.append(other_outcomes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary_outcomes is not UNSET:
            field_dict["primaryOutcomes"] = primary_outcomes
        if secondary_outcomes is not UNSET:
            field_dict["secondaryOutcomes"] = secondary_outcomes
        if other_outcomes is not UNSET:
            field_dict["otherOutcomes"] = other_outcomes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.outcome import Outcome

        d = src_dict.copy()
        primary_outcomes = []
        _primary_outcomes = d.pop("primaryOutcomes", UNSET)
        for primary_outcomes_item_data in _primary_outcomes or []:
            primary_outcomes_item = Outcome.from_dict(primary_outcomes_item_data)

            primary_outcomes.append(primary_outcomes_item)

        secondary_outcomes = []
        _secondary_outcomes = d.pop("secondaryOutcomes", UNSET)
        for secondary_outcomes_item_data in _secondary_outcomes or []:
            secondary_outcomes_item = Outcome.from_dict(secondary_outcomes_item_data)

            secondary_outcomes.append(secondary_outcomes_item)

        other_outcomes = []
        _other_outcomes = d.pop("otherOutcomes", UNSET)
        for other_outcomes_item_data in _other_outcomes or []:
            other_outcomes_item = Outcome.from_dict(other_outcomes_item_data)

            other_outcomes.append(other_outcomes_item)

        outcomes_module = cls(
            primary_outcomes=primary_outcomes,
            secondary_outcomes=secondary_outcomes,
            other_outcomes=other_outcomes,
        )

        outcomes_module.additional_properties = d
        return outcomes_module

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
