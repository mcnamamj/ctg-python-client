from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sampling_method import SamplingMethod
from ..models.sex import Sex
from ..models.standard_age import StandardAge
from ..types import UNSET, Unset

T = TypeVar("T", bound="EligibilityModule")


@_attrs_define
class EligibilityModule:
    """
    Attributes:
        eligibility_criteria (Union[Unset, str]):
        healthy_volunteers (Union[Unset, bool]):
        sex (Union[Unset, Sex]):
        gender_based (Union[Unset, bool]):
        gender_description (Union[Unset, str]):
        minimum_age (Union[Unset, str]):
        maximum_age (Union[Unset, str]):
        std_ages (Union[Unset, List[StandardAge]]):
        study_population (Union[Unset, str]):
        sampling_method (Union[Unset, SamplingMethod]):
    """

    eligibility_criteria: Union[Unset, str] = UNSET
    healthy_volunteers: Union[Unset, bool] = UNSET
    sex: Union[Unset, Sex] = UNSET
    gender_based: Union[Unset, bool] = UNSET
    gender_description: Union[Unset, str] = UNSET
    minimum_age: Union[Unset, str] = UNSET
    maximum_age: Union[Unset, str] = UNSET
    std_ages: Union[Unset, List[StandardAge]] = UNSET
    study_population: Union[Unset, str] = UNSET
    sampling_method: Union[Unset, SamplingMethod] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eligibility_criteria = self.eligibility_criteria

        healthy_volunteers = self.healthy_volunteers

        sex: Union[Unset, str] = UNSET
        if not isinstance(self.sex, Unset):
            sex = self.sex.value

        gender_based = self.gender_based

        gender_description = self.gender_description

        minimum_age = self.minimum_age

        maximum_age = self.maximum_age

        std_ages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.std_ages, Unset):
            std_ages = []
            for std_ages_item_data in self.std_ages:
                std_ages_item = std_ages_item_data.value
                std_ages.append(std_ages_item)

        study_population = self.study_population

        sampling_method: Union[Unset, str] = UNSET
        if not isinstance(self.sampling_method, Unset):
            sampling_method = self.sampling_method.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eligibility_criteria is not UNSET:
            field_dict["eligibilityCriteria"] = eligibility_criteria
        if healthy_volunteers is not UNSET:
            field_dict["healthyVolunteers"] = healthy_volunteers
        if sex is not UNSET:
            field_dict["sex"] = sex
        if gender_based is not UNSET:
            field_dict["genderBased"] = gender_based
        if gender_description is not UNSET:
            field_dict["genderDescription"] = gender_description
        if minimum_age is not UNSET:
            field_dict["minimumAge"] = minimum_age
        if maximum_age is not UNSET:
            field_dict["maximumAge"] = maximum_age
        if std_ages is not UNSET:
            field_dict["stdAges"] = std_ages
        if study_population is not UNSET:
            field_dict["studyPopulation"] = study_population
        if sampling_method is not UNSET:
            field_dict["samplingMethod"] = sampling_method

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eligibility_criteria = d.pop("eligibilityCriteria", UNSET)

        healthy_volunteers = d.pop("healthyVolunteers", UNSET)

        _sex = d.pop("sex", UNSET)
        sex: Union[Unset, Sex]
        if isinstance(_sex, Unset):
            sex = UNSET
        else:
            sex = Sex(_sex)

        gender_based = d.pop("genderBased", UNSET)

        gender_description = d.pop("genderDescription", UNSET)

        minimum_age = d.pop("minimumAge", UNSET)

        maximum_age = d.pop("maximumAge", UNSET)

        std_ages = []
        _std_ages = d.pop("stdAges", UNSET)
        for std_ages_item_data in _std_ages or []:
            std_ages_item = StandardAge(std_ages_item_data)

            std_ages.append(std_ages_item)

        study_population = d.pop("studyPopulation", UNSET)

        _sampling_method = d.pop("samplingMethod", UNSET)
        sampling_method: Union[Unset, SamplingMethod]
        if isinstance(_sampling_method, Unset):
            sampling_method = UNSET
        else:
            sampling_method = SamplingMethod(_sampling_method)

        eligibility_module = cls(
            eligibility_criteria=eligibility_criteria,
            healthy_volunteers=healthy_volunteers,
            sex=sex,
            gender_based=gender_based,
            gender_description=gender_description,
            minimum_age=minimum_age,
            maximum_age=maximum_age,
            std_ages=std_ages,
            study_population=study_population,
            sampling_method=sampling_method,
        )

        eligibility_module.additional_properties = d
        return eligibility_module

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
