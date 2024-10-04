from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.phase import Phase
from ..models.study_type import StudyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bio_spec import BioSpec
    from ..models.design_info import DesignInfo
    from ..models.enrollment_info import EnrollmentInfo
    from ..models.expanded_access_types import ExpandedAccessTypes


T = TypeVar("T", bound="DesignModule")


@_attrs_define
class DesignModule:
    """
    Attributes:
        study_type (Union[Unset, StudyType]):
        n_ptrs_to_this_exp_acc_nct_id (Union[Unset, float]):
        expanded_access_types (Union[Unset, ExpandedAccessTypes]):
        patient_registry (Union[Unset, bool]):
        target_duration (Union[Unset, str]):
        phases (Union[Unset, List[Phase]]):
        design_info (Union[Unset, DesignInfo]):
        bio_spec (Union[Unset, BioSpec]):
        enrollment_info (Union[Unset, EnrollmentInfo]):
    """

    study_type: Union[Unset, StudyType] = UNSET
    n_ptrs_to_this_exp_acc_nct_id: Union[Unset, float] = UNSET
    expanded_access_types: Union[Unset, "ExpandedAccessTypes"] = UNSET
    patient_registry: Union[Unset, bool] = UNSET
    target_duration: Union[Unset, str] = UNSET
    phases: Union[Unset, List[Phase]] = UNSET
    design_info: Union[Unset, "DesignInfo"] = UNSET
    bio_spec: Union[Unset, "BioSpec"] = UNSET
    enrollment_info: Union[Unset, "EnrollmentInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        study_type: Union[Unset, str] = UNSET
        if not isinstance(self.study_type, Unset):
            study_type = self.study_type.value

        n_ptrs_to_this_exp_acc_nct_id = self.n_ptrs_to_this_exp_acc_nct_id

        expanded_access_types: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expanded_access_types, Unset):
            expanded_access_types = self.expanded_access_types.to_dict()

        patient_registry = self.patient_registry

        target_duration = self.target_duration

        phases: Union[Unset, List[str]] = UNSET
        if not isinstance(self.phases, Unset):
            phases = []
            for phases_item_data in self.phases:
                phases_item = phases_item_data.value
                phases.append(phases_item)

        design_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.design_info, Unset):
            design_info = self.design_info.to_dict()

        bio_spec: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.bio_spec, Unset):
            bio_spec = self.bio_spec.to_dict()

        enrollment_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.enrollment_info, Unset):
            enrollment_info = self.enrollment_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if study_type is not UNSET:
            field_dict["studyType"] = study_type
        if n_ptrs_to_this_exp_acc_nct_id is not UNSET:
            field_dict["nPtrsToThisExpAccNctId"] = n_ptrs_to_this_exp_acc_nct_id
        if expanded_access_types is not UNSET:
            field_dict["expandedAccessTypes"] = expanded_access_types
        if patient_registry is not UNSET:
            field_dict["patientRegistry"] = patient_registry
        if target_duration is not UNSET:
            field_dict["targetDuration"] = target_duration
        if phases is not UNSET:
            field_dict["phases"] = phases
        if design_info is not UNSET:
            field_dict["designInfo"] = design_info
        if bio_spec is not UNSET:
            field_dict["bioSpec"] = bio_spec
        if enrollment_info is not UNSET:
            field_dict["enrollmentInfo"] = enrollment_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.bio_spec import BioSpec
        from ..models.design_info import DesignInfo
        from ..models.enrollment_info import EnrollmentInfo
        from ..models.expanded_access_types import ExpandedAccessTypes

        d = src_dict.copy()
        _study_type = d.pop("studyType", UNSET)
        study_type: Union[Unset, StudyType]
        if isinstance(_study_type, Unset):
            study_type = UNSET
        else:
            study_type = StudyType(_study_type)

        n_ptrs_to_this_exp_acc_nct_id = d.pop("nPtrsToThisExpAccNctId", UNSET)

        _expanded_access_types = d.pop("expandedAccessTypes", UNSET)
        expanded_access_types: Union[Unset, ExpandedAccessTypes]
        if isinstance(_expanded_access_types, Unset):
            expanded_access_types = UNSET
        else:
            expanded_access_types = ExpandedAccessTypes.from_dict(_expanded_access_types)

        patient_registry = d.pop("patientRegistry", UNSET)

        target_duration = d.pop("targetDuration", UNSET)

        phases = []
        _phases = d.pop("phases", UNSET)
        for phases_item_data in _phases or []:
            phases_item = Phase(phases_item_data)

            phases.append(phases_item)

        _design_info = d.pop("designInfo", UNSET)
        design_info: Union[Unset, DesignInfo]
        if isinstance(_design_info, Unset):
            design_info = UNSET
        else:
            design_info = DesignInfo.from_dict(_design_info)

        _bio_spec = d.pop("bioSpec", UNSET)
        bio_spec: Union[Unset, BioSpec]
        if isinstance(_bio_spec, Unset):
            bio_spec = UNSET
        else:
            bio_spec = BioSpec.from_dict(_bio_spec)

        _enrollment_info = d.pop("enrollmentInfo", UNSET)
        enrollment_info: Union[Unset, EnrollmentInfo]
        if isinstance(_enrollment_info, Unset):
            enrollment_info = UNSET
        else:
            enrollment_info = EnrollmentInfo.from_dict(_enrollment_info)

        design_module = cls(
            study_type=study_type,
            n_ptrs_to_this_exp_acc_nct_id=n_ptrs_to_this_exp_acc_nct_id,
            expanded_access_types=expanded_access_types,
            patient_registry=patient_registry,
            target_duration=target_duration,
            phases=phases,
            design_info=design_info,
            bio_spec=bio_spec,
            enrollment_info=enrollment_info,
        )

        design_module.additional_properties = d
        return design_module

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
