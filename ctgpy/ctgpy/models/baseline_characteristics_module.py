from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.baseline_measure import BaselineMeasure
    from ..models.denom import Denom
    from ..models.measure_group import MeasureGroup


T = TypeVar("T", bound="BaselineCharacteristicsModule")


@_attrs_define
class BaselineCharacteristicsModule:
    """
    Attributes:
        population_description (Union[Unset, str]):
        type_units_analyzed (Union[Unset, str]):
        groups (Union[Unset, List['MeasureGroup']]):
        denoms (Union[Unset, List['Denom']]):
        measures (Union[Unset, List['BaselineMeasure']]):
    """

    population_description: Union[Unset, str] = UNSET
    type_units_analyzed: Union[Unset, str] = UNSET
    groups: Union[Unset, List["MeasureGroup"]] = UNSET
    denoms: Union[Unset, List["Denom"]] = UNSET
    measures: Union[Unset, List["BaselineMeasure"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        population_description = self.population_description

        type_units_analyzed = self.type_units_analyzed

        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)

        denoms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.denoms, Unset):
            denoms = []
            for denoms_item_data in self.denoms:
                denoms_item = denoms_item_data.to_dict()
                denoms.append(denoms_item)

        measures: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measures, Unset):
            measures = []
            for measures_item_data in self.measures:
                measures_item = measures_item_data.to_dict()
                measures.append(measures_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if population_description is not UNSET:
            field_dict["populationDescription"] = population_description
        if type_units_analyzed is not UNSET:
            field_dict["typeUnitsAnalyzed"] = type_units_analyzed
        if groups is not UNSET:
            field_dict["groups"] = groups
        if denoms is not UNSET:
            field_dict["denoms"] = denoms
        if measures is not UNSET:
            field_dict["measures"] = measures

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.baseline_measure import BaselineMeasure
        from ..models.denom import Denom
        from ..models.measure_group import MeasureGroup

        d = src_dict.copy()
        population_description = d.pop("populationDescription", UNSET)

        type_units_analyzed = d.pop("typeUnitsAnalyzed", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = MeasureGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        denoms = []
        _denoms = d.pop("denoms", UNSET)
        for denoms_item_data in _denoms or []:
            denoms_item = Denom.from_dict(denoms_item_data)

            denoms.append(denoms_item)

        measures = []
        _measures = d.pop("measures", UNSET)
        for measures_item_data in _measures or []:
            measures_item = BaselineMeasure.from_dict(measures_item_data)

            measures.append(measures_item)

        baseline_characteristics_module = cls(
            population_description=population_description,
            type_units_analyzed=type_units_analyzed,
            groups=groups,
            denoms=denoms,
            measures=measures,
        )

        baseline_characteristics_module.additional_properties = d
        return baseline_characteristics_module

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
