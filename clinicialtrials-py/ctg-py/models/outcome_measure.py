from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.measure_param import MeasureParam
from ..models.outcome_measure_type import OutcomeMeasureType
from ..models.reporting_status import ReportingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.denom import Denom
    from ..models.measure_analysis import MeasureAnalysis
    from ..models.measure_class import MeasureClass
    from ..models.measure_group import MeasureGroup


T = TypeVar("T", bound="OutcomeMeasure")


@_attrs_define
class OutcomeMeasure:
    """
    Attributes:
        type (Union[Unset, OutcomeMeasureType]):
        title (Union[Unset, str]):
        description (Union[Unset, str]):
        population_description (Union[Unset, str]):
        reporting_status (Union[Unset, ReportingStatus]):
        anticipated_posting_date (Union[Unset, str]): Date in `yyyy`, `yyyy-MM`, or `yyyy-MM-dd` format
        param_type (Union[Unset, MeasureParam]):
        dispersion_type (Union[Unset, str]):
        unit_of_measure (Union[Unset, str]):
        calculate_pct (Union[Unset, bool]):
        time_frame (Union[Unset, str]):
        type_units_analyzed (Union[Unset, str]):
        denom_units_selected (Union[Unset, str]):
        groups (Union[Unset, List['MeasureGroup']]):
        denoms (Union[Unset, List['Denom']]):
        classes (Union[Unset, List['MeasureClass']]):
        analyses (Union[Unset, List['MeasureAnalysis']]):
    """

    type: Union[Unset, OutcomeMeasureType] = UNSET
    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    population_description: Union[Unset, str] = UNSET
    reporting_status: Union[Unset, ReportingStatus] = UNSET
    anticipated_posting_date: Union[Unset, str] = UNSET
    param_type: Union[Unset, MeasureParam] = UNSET
    dispersion_type: Union[Unset, str] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    calculate_pct: Union[Unset, bool] = UNSET
    time_frame: Union[Unset, str] = UNSET
    type_units_analyzed: Union[Unset, str] = UNSET
    denom_units_selected: Union[Unset, str] = UNSET
    groups: Union[Unset, List["MeasureGroup"]] = UNSET
    denoms: Union[Unset, List["Denom"]] = UNSET
    classes: Union[Unset, List["MeasureClass"]] = UNSET
    analyses: Union[Unset, List["MeasureAnalysis"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        title = self.title

        description = self.description

        population_description = self.population_description

        reporting_status: Union[Unset, str] = UNSET
        if not isinstance(self.reporting_status, Unset):
            reporting_status = self.reporting_status.value

        anticipated_posting_date = self.anticipated_posting_date

        param_type: Union[Unset, str] = UNSET
        if not isinstance(self.param_type, Unset):
            param_type = self.param_type.value

        dispersion_type = self.dispersion_type

        unit_of_measure = self.unit_of_measure

        calculate_pct = self.calculate_pct

        time_frame = self.time_frame

        type_units_analyzed = self.type_units_analyzed

        denom_units_selected = self.denom_units_selected

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

        classes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.classes, Unset):
            classes = []
            for classes_item_data in self.classes:
                classes_item = classes_item_data.to_dict()
                classes.append(classes_item)

        analyses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.analyses, Unset):
            analyses = []
            for analyses_item_data in self.analyses:
                analyses_item = analyses_item_data.to_dict()
                analyses.append(analyses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if population_description is not UNSET:
            field_dict["populationDescription"] = population_description
        if reporting_status is not UNSET:
            field_dict["reportingStatus"] = reporting_status
        if anticipated_posting_date is not UNSET:
            field_dict["anticipatedPostingDate"] = anticipated_posting_date
        if param_type is not UNSET:
            field_dict["paramType"] = param_type
        if dispersion_type is not UNSET:
            field_dict["dispersionType"] = dispersion_type
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if calculate_pct is not UNSET:
            field_dict["calculatePct"] = calculate_pct
        if time_frame is not UNSET:
            field_dict["timeFrame"] = time_frame
        if type_units_analyzed is not UNSET:
            field_dict["typeUnitsAnalyzed"] = type_units_analyzed
        if denom_units_selected is not UNSET:
            field_dict["denomUnitsSelected"] = denom_units_selected
        if groups is not UNSET:
            field_dict["groups"] = groups
        if denoms is not UNSET:
            field_dict["denoms"] = denoms
        if classes is not UNSET:
            field_dict["classes"] = classes
        if analyses is not UNSET:
            field_dict["analyses"] = analyses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.denom import Denom
        from ..models.measure_analysis import MeasureAnalysis
        from ..models.measure_class import MeasureClass
        from ..models.measure_group import MeasureGroup

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, OutcomeMeasureType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = OutcomeMeasureType(_type)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        population_description = d.pop("populationDescription", UNSET)

        _reporting_status = d.pop("reportingStatus", UNSET)
        reporting_status: Union[Unset, ReportingStatus]
        if isinstance(_reporting_status, Unset):
            reporting_status = UNSET
        else:
            reporting_status = ReportingStatus(_reporting_status)

        anticipated_posting_date = d.pop("anticipatedPostingDate", UNSET)

        _param_type = d.pop("paramType", UNSET)
        param_type: Union[Unset, MeasureParam]
        if isinstance(_param_type, Unset):
            param_type = UNSET
        else:
            param_type = MeasureParam(_param_type)

        dispersion_type = d.pop("dispersionType", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        calculate_pct = d.pop("calculatePct", UNSET)

        time_frame = d.pop("timeFrame", UNSET)

        type_units_analyzed = d.pop("typeUnitsAnalyzed", UNSET)

        denom_units_selected = d.pop("denomUnitsSelected", UNSET)

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

        classes = []
        _classes = d.pop("classes", UNSET)
        for classes_item_data in _classes or []:
            classes_item = MeasureClass.from_dict(classes_item_data)

            classes.append(classes_item)

        analyses = []
        _analyses = d.pop("analyses", UNSET)
        for analyses_item_data in _analyses or []:
            analyses_item = MeasureAnalysis.from_dict(analyses_item_data)

            analyses.append(analyses_item)

        outcome_measure = cls(
            type=type,
            title=title,
            description=description,
            population_description=population_description,
            reporting_status=reporting_status,
            anticipated_posting_date=anticipated_posting_date,
            param_type=param_type,
            dispersion_type=dispersion_type,
            unit_of_measure=unit_of_measure,
            calculate_pct=calculate_pct,
            time_frame=time_frame,
            type_units_analyzed=type_units_analyzed,
            denom_units_selected=denom_units_selected,
            groups=groups,
            denoms=denoms,
            classes=classes,
            analyses=analyses,
        )

        outcome_measure.additional_properties = d
        return outcome_measure

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
