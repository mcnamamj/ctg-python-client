from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventGroup")


@_attrs_define
class EventGroup:
    """
    Attributes:
        id (Union[Unset, str]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        deaths_num_affected (Union[Unset, int]):
        deaths_num_at_risk (Union[Unset, int]):
        serious_num_affected (Union[Unset, int]):
        serious_num_at_risk (Union[Unset, int]):
        other_num_affected (Union[Unset, int]):
        other_num_at_risk (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    deaths_num_affected: Union[Unset, int] = UNSET
    deaths_num_at_risk: Union[Unset, int] = UNSET
    serious_num_affected: Union[Unset, int] = UNSET
    serious_num_at_risk: Union[Unset, int] = UNSET
    other_num_affected: Union[Unset, int] = UNSET
    other_num_at_risk: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        title = self.title

        description = self.description

        deaths_num_affected = self.deaths_num_affected

        deaths_num_at_risk = self.deaths_num_at_risk

        serious_num_affected = self.serious_num_affected

        serious_num_at_risk = self.serious_num_at_risk

        other_num_affected = self.other_num_affected

        other_num_at_risk = self.other_num_at_risk

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if deaths_num_affected is not UNSET:
            field_dict["deathsNumAffected"] = deaths_num_affected
        if deaths_num_at_risk is not UNSET:
            field_dict["deathsNumAtRisk"] = deaths_num_at_risk
        if serious_num_affected is not UNSET:
            field_dict["seriousNumAffected"] = serious_num_affected
        if serious_num_at_risk is not UNSET:
            field_dict["seriousNumAtRisk"] = serious_num_at_risk
        if other_num_affected is not UNSET:
            field_dict["otherNumAffected"] = other_num_affected
        if other_num_at_risk is not UNSET:
            field_dict["otherNumAtRisk"] = other_num_at_risk

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        deaths_num_affected = d.pop("deathsNumAffected", UNSET)

        deaths_num_at_risk = d.pop("deathsNumAtRisk", UNSET)

        serious_num_affected = d.pop("seriousNumAffected", UNSET)

        serious_num_at_risk = d.pop("seriousNumAtRisk", UNSET)

        other_num_affected = d.pop("otherNumAffected", UNSET)

        other_num_at_risk = d.pop("otherNumAtRisk", UNSET)

        event_group = cls(
            id=id,
            title=title,
            description=description,
            deaths_num_affected=deaths_num_affected,
            deaths_num_at_risk=deaths_num_at_risk,
            serious_num_affected=serious_num_affected,
            serious_num_at_risk=serious_num_at_risk,
            other_num_affected=other_num_affected,
            other_num_at_risk=other_num_at_risk,
        )

        event_group.additional_properties = d
        return event_group

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
