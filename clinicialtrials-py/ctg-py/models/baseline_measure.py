from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.measure_dispersion_type import MeasureDispersionType
from ..models.measure_param import MeasureParam
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.denom import Denom
    from ..models.measure_class import MeasureClass


T = TypeVar("T", bound="BaselineMeasure")


@_attrs_define
class BaselineMeasure:
    """
    Attributes:
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        population_description (Union[Unset, str]):
        param_type (Union[Unset, MeasureParam]):
        dispersion_type (Union[Unset, MeasureDispersionType]):
        unit_of_measure (Union[Unset, str]):
        calculate_pct (Union[Unset, bool]):
        denom_units_selected (Union[Unset, str]):
        denoms (Union[Unset, List['Denom']]):
        classes (Union[Unset, List['MeasureClass']]):
    """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    population_description: Union[Unset, str] = UNSET
    param_type: Union[Unset, MeasureParam] = UNSET
    dispersion_type: Union[Unset, MeasureDispersionType] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    calculate_pct: Union[Unset, bool] = UNSET
    denom_units_selected: Union[Unset, str] = UNSET
    denoms: Union[Unset, List["Denom"]] = UNSET
    classes: Union[Unset, List["MeasureClass"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        description = self.description

        population_description = self.population_description

        param_type: Union[Unset, str] = UNSET
        if not isinstance(self.param_type, Unset):
            param_type = self.param_type.value

        dispersion_type: Union[Unset, str] = UNSET
        if not isinstance(self.dispersion_type, Unset):
            dispersion_type = self.dispersion_type.value

        unit_of_measure = self.unit_of_measure

        calculate_pct = self.calculate_pct

        denom_units_selected = self.denom_units_selected

        denoms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.denoms, Unset):
            denoms = []
            for denoms_item_data in self.denoms:
                denoms_item = denoms_item_data.to_dict()
                denoms.append(denoms_item)

        classes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = []
            for classes_item_data in self.classes:
                classes_item = classes_item_data.to_dict()
                classes.append(classes_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if population_description is not UNSET:
            field_dict["populationDescription"] = population_description
        if param_type is not UNSET:
            field_dict["paramType"] = param_type
        if dispersion_type is not UNSET:
            field_dict["dispersionType"] = dispersion_type
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if calculate_pct is not UNSET:
            field_dict["calculatePct"] = calculate_pct
        if denom_units_selected is not UNSET:
            field_dict["denomUnitsSelected"] = denom_units_selected
        if denoms is not UNSET:
            field_dict["denoms"] = denoms
        if classes is not UNSET:
            field_dict["classes"] = classes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.denom import Denom
        from ..models.measure_class import MeasureClass

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        population_description = d.pop("populationDescription", UNSET)

        _param_type = d.pop("paramType", UNSET)
        param_type: Union[Unset, MeasureParam]
        if isinstance(_param_type, Unset):
            param_type = UNSET
        else:
            param_type = MeasureParam(_param_type)

        _dispersion_type = d.pop("dispersionType", UNSET)
        dispersion_type: Union[Unset, MeasureDispersionType]
        if isinstance(_dispersion_type, Unset):
            dispersion_type = UNSET
        else:
            dispersion_type = MeasureDispersionType(_dispersion_type)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        calculate_pct = d.pop("calculatePct", UNSET)

        denom_units_selected = d.pop("denomUnitsSelected", UNSET)

        denoms = []
        _denoms = d.pop("denoms", UNSET)
        for denoms_item_data in _denoms or []:
            denoms_item = Denom.from_dict(denoms_item_data)

            denoms.append(denoms_item)

        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = MeasureClass.from_dict(classes_item_data)

            classes.append(classes_item)

        baseline_measure = cls(
            title=title,
            description=description,
            population_description=population_description,
            param_type=param_type,
            dispersion_type=dispersion_type,
            unit_of_measure=unit_of_measure,
            calculate_pct=calculate_pct,
            denom_units_selected=denom_units_selected,
            denoms=denoms,
            classes=classes,
        )

        baseline_measure.additional_properties = d
        return baseline_measure

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
