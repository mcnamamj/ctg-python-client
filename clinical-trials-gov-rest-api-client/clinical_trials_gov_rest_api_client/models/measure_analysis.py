from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.analysis_dispersion_type import AnalysisDispersionType
from ..models.confidence_interval_num_sides import ConfidenceIntervalNumSides
from ..models.non_inferiority_type import NonInferiorityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MeasureAnalysis")


@_attrs_define
class MeasureAnalysis:
    """
    Attributes:
        param_type (Union[Unset, str]):
        param_value (Union[Unset, str]):
        dispersion_type (Union[Unset, AnalysisDispersionType]):
        dispersion_value (Union[Unset, str]):
        statistical_method (Union[Unset, str]):
        statistical_comment (Union[Unset, str]):
        p_value (Union[Unset, str]):
        p_value_comment (Union[Unset, str]):
        ci_num_sides (Union[Unset, ConfidenceIntervalNumSides]):
        ci_pct_value (Union[Unset, str]):
        ci_lower_limit (Union[Unset, str]):
        ci_upper_limit (Union[Unset, str]):
        ci_lower_limit_comment (Union[Unset, str]):
        ci_upper_limit_comment (Union[Unset, str]):
        estimate_comment (Union[Unset, str]):
        tested_non_inferiority (Union[Unset, bool]):
        non_inferiority_type (Union[Unset, NonInferiorityType]):
        non_inferiority_comment (Union[Unset, str]):
        other_analysis_description (Union[Unset, str]):
        group_description (Union[Unset, str]):
        group_ids (Union[Unset, List[str]]):
    """

    param_type: Union[Unset, str] = UNSET
    param_value: Union[Unset, str] = UNSET
    dispersion_type: Union[Unset, AnalysisDispersionType] = UNSET
    dispersion_value: Union[Unset, str] = UNSET
    statistical_method: Union[Unset, str] = UNSET
    statistical_comment: Union[Unset, str] = UNSET
    p_value: Union[Unset, str] = UNSET
    p_value_comment: Union[Unset, str] = UNSET
    ci_num_sides: Union[Unset, ConfidenceIntervalNumSides] = UNSET
    ci_pct_value: Union[Unset, str] = UNSET
    ci_lower_limit: Union[Unset, str] = UNSET
    ci_upper_limit: Union[Unset, str] = UNSET
    ci_lower_limit_comment: Union[Unset, str] = UNSET
    ci_upper_limit_comment: Union[Unset, str] = UNSET
    estimate_comment: Union[Unset, str] = UNSET
    tested_non_inferiority: Union[Unset, bool] = UNSET
    non_inferiority_type: Union[Unset, NonInferiorityType] = UNSET
    non_inferiority_comment: Union[Unset, str] = UNSET
    other_analysis_description: Union[Unset, str] = UNSET
    group_description: Union[Unset, str] = UNSET
    group_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        param_type = self.param_type

        param_value = self.param_value

        dispersion_type: Union[Unset, str] = UNSET
        if not isinstance(self.dispersion_type, Unset):
            dispersion_type = self.dispersion_type.value

        dispersion_value = self.dispersion_value

        statistical_method = self.statistical_method

        statistical_comment = self.statistical_comment

        p_value = self.p_value

        p_value_comment = self.p_value_comment

        ci_num_sides: Union[Unset, str] = UNSET
        if not isinstance(self.ci_num_sides, Unset):
            ci_num_sides = self.ci_num_sides.value

        ci_pct_value = self.ci_pct_value

        ci_lower_limit = self.ci_lower_limit

        ci_upper_limit = self.ci_upper_limit

        ci_lower_limit_comment = self.ci_lower_limit_comment

        ci_upper_limit_comment = self.ci_upper_limit_comment

        estimate_comment = self.estimate_comment

        tested_non_inferiority = self.tested_non_inferiority

        non_inferiority_type: Union[Unset, str] = UNSET
        if not isinstance(self.non_inferiority_type, Unset):
            non_inferiority_type = self.non_inferiority_type.value

        non_inferiority_comment = self.non_inferiority_comment

        other_analysis_description = self.other_analysis_description

        group_description = self.group_description

        group_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if param_type is not UNSET:
            field_dict["paramType"] = param_type
        if param_value is not UNSET:
            field_dict["paramValue"] = param_value
        if dispersion_type is not UNSET:
            field_dict["dispersionType"] = dispersion_type
        if dispersion_value is not UNSET:
            field_dict["dispersionValue"] = dispersion_value
        if statistical_method is not UNSET:
            field_dict["statisticalMethod"] = statistical_method
        if statistical_comment is not UNSET:
            field_dict["statisticalComment"] = statistical_comment
        if p_value is not UNSET:
            field_dict["pValue"] = p_value
        if p_value_comment is not UNSET:
            field_dict["pValueComment"] = p_value_comment
        if ci_num_sides is not UNSET:
            field_dict["ciNumSides"] = ci_num_sides
        if ci_pct_value is not UNSET:
            field_dict["ciPctValue"] = ci_pct_value
        if ci_lower_limit is not UNSET:
            field_dict["ciLowerLimit"] = ci_lower_limit
        if ci_upper_limit is not UNSET:
            field_dict["ciUpperLimit"] = ci_upper_limit
        if ci_lower_limit_comment is not UNSET:
            field_dict["ciLowerLimitComment"] = ci_lower_limit_comment
        if ci_upper_limit_comment is not UNSET:
            field_dict["ciUpperLimitComment"] = ci_upper_limit_comment
        if estimate_comment is not UNSET:
            field_dict["estimateComment"] = estimate_comment
        if tested_non_inferiority is not UNSET:
            field_dict["testedNonInferiority"] = tested_non_inferiority
        if non_inferiority_type is not UNSET:
            field_dict["nonInferiorityType"] = non_inferiority_type
        if non_inferiority_comment is not UNSET:
            field_dict["nonInferiorityComment"] = non_inferiority_comment
        if other_analysis_description is not UNSET:
            field_dict["otherAnalysisDescription"] = other_analysis_description
        if group_description is not UNSET:
            field_dict["groupDescription"] = group_description
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        param_type = d.pop("paramType", UNSET)

        param_value = d.pop("paramValue", UNSET)

        _dispersion_type = d.pop("dispersionType", UNSET)
        dispersion_type: Union[Unset, AnalysisDispersionType]
        if isinstance(_dispersion_type, Unset):
            dispersion_type = UNSET
        else:
            dispersion_type = AnalysisDispersionType(_dispersion_type)

        dispersion_value = d.pop("dispersionValue", UNSET)

        statistical_method = d.pop("statisticalMethod", UNSET)

        statistical_comment = d.pop("statisticalComment", UNSET)

        p_value = d.pop("pValue", UNSET)

        p_value_comment = d.pop("pValueComment", UNSET)

        _ci_num_sides = d.pop("ciNumSides", UNSET)
        ci_num_sides: Union[Unset, ConfidenceIntervalNumSides]
        if isinstance(_ci_num_sides, Unset):
            ci_num_sides = UNSET
        else:
            ci_num_sides = ConfidenceIntervalNumSides(_ci_num_sides)

        ci_pct_value = d.pop("ciPctValue", UNSET)

        ci_lower_limit = d.pop("ciLowerLimit", UNSET)

        ci_upper_limit = d.pop("ciUpperLimit", UNSET)

        ci_lower_limit_comment = d.pop("ciLowerLimitComment", UNSET)

        ci_upper_limit_comment = d.pop("ciUpperLimitComment", UNSET)

        estimate_comment = d.pop("estimateComment", UNSET)

        tested_non_inferiority = d.pop("testedNonInferiority", UNSET)

        _non_inferiority_type = d.pop("nonInferiorityType", UNSET)
        non_inferiority_type: Union[Unset, NonInferiorityType]
        if isinstance(_non_inferiority_type, Unset):
            non_inferiority_type = UNSET
        else:
            non_inferiority_type = NonInferiorityType(_non_inferiority_type)

        non_inferiority_comment = d.pop("nonInferiorityComment", UNSET)

        other_analysis_description = d.pop("otherAnalysisDescription", UNSET)

        group_description = d.pop("groupDescription", UNSET)

        group_ids = cast(List[str], d.pop("groupIds", UNSET))

        measure_analysis = cls(
            param_type=param_type,
            param_value=param_value,
            dispersion_type=dispersion_type,
            dispersion_value=dispersion_value,
            statistical_method=statistical_method,
            statistical_comment=statistical_comment,
            p_value=p_value,
            p_value_comment=p_value_comment,
            ci_num_sides=ci_num_sides,
            ci_pct_value=ci_pct_value,
            ci_lower_limit=ci_lower_limit,
            ci_upper_limit=ci_upper_limit,
            ci_lower_limit_comment=ci_lower_limit_comment,
            ci_upper_limit_comment=ci_upper_limit_comment,
            estimate_comment=estimate_comment,
            tested_non_inferiority=tested_non_inferiority,
            non_inferiority_type=non_inferiority_type,
            non_inferiority_comment=non_inferiority_comment,
            other_analysis_description=other_analysis_description,
            group_description=group_description,
            group_ids=group_ids,
        )

        measure_analysis.additional_properties = d
        return measure_analysis

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
