from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.design_allocation import DesignAllocation
from ..models.design_time_perspective import DesignTimePerspective
from ..models.interventional_assignment import InterventionalAssignment
from ..models.observational_model import ObservationalModel
from ..models.primary_purpose import PrimaryPurpose
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.masking_block import MaskingBlock


T = TypeVar("T", bound="DesignInfo")


@_attrs_define
class DesignInfo:
    """
    Attributes:
        allocation (Union[Unset, DesignAllocation]):
        intervention_model (Union[Unset, InterventionalAssignment]):
        intervention_model_description (Union[Unset, str]):
        primary_purpose (Union[Unset, PrimaryPurpose]):
        observational_model (Union[Unset, ObservationalModel]):
        time_perspective (Union[Unset, DesignTimePerspective]):
        masking_info (Union[Unset, MaskingBlock]):
    """

    allocation: Union[Unset, DesignAllocation] = UNSET
    intervention_model: Union[Unset, InterventionalAssignment] = UNSET
    intervention_model_description: Union[Unset, str] = UNSET
    primary_purpose: Union[Unset, PrimaryPurpose] = UNSET
    observational_model: Union[Unset, ObservationalModel] = UNSET
    time_perspective: Union[Unset, DesignTimePerspective] = UNSET
    masking_info: Union[Unset, "MaskingBlock"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        allocation: Union[Unset, str] = UNSET
        if not isinstance(self.allocation, Unset):
            allocation = self.allocation.value

        intervention_model: Union[Unset, str] = UNSET
        if not isinstance(self.intervention_model, Unset):
            intervention_model = self.intervention_model.value

        intervention_model_description = self.intervention_model_description

        primary_purpose: Union[Unset, str] = UNSET
        if not isinstance(self.primary_purpose, Unset):
            primary_purpose = self.primary_purpose.value

        observational_model: Union[Unset, str] = UNSET
        if not isinstance(self.observational_model, Unset):
            observational_model = self.observational_model.value

        time_perspective: Union[Unset, str] = UNSET
        if not isinstance(self.time_perspective, Unset):
            time_perspective = self.time_perspective.value

        masking_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.masking_info, Unset):
            masking_info = self.masking_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocation is not UNSET:
            field_dict["allocation"] = allocation
        if intervention_model is not UNSET:
            field_dict["interventionModel"] = intervention_model
        if intervention_model_description is not UNSET:
            field_dict["interventionModelDescription"] = intervention_model_description
        if primary_purpose is not UNSET:
            field_dict["primaryPurpose"] = primary_purpose
        if observational_model is not UNSET:
            field_dict["observationalModel"] = observational_model
        if time_perspective is not UNSET:
            field_dict["timePerspective"] = time_perspective
        if masking_info is not UNSET:
            field_dict["maskingInfo"] = masking_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.masking_block import MaskingBlock

        d = src_dict.copy()
        _allocation = d.pop("allocation", UNSET)
        allocation: Union[Unset, DesignAllocation]
        if isinstance(_allocation, Unset):
            allocation = UNSET
        else:
            allocation = DesignAllocation(_allocation)

        _intervention_model = d.pop("interventionModel", UNSET)
        intervention_model: Union[Unset, InterventionalAssignment]
        if isinstance(_intervention_model, Unset):
            intervention_model = UNSET
        else:
            intervention_model = InterventionalAssignment(_intervention_model)

        intervention_model_description = d.pop("interventionModelDescription", UNSET)

        _primary_purpose = d.pop("primaryPurpose", UNSET)
        primary_purpose: Union[Unset, PrimaryPurpose]
        if isinstance(_primary_purpose, Unset):
            primary_purpose = UNSET
        else:
            primary_purpose = PrimaryPurpose(_primary_purpose)

        _observational_model = d.pop("observationalModel", UNSET)
        observational_model: Union[Unset, ObservationalModel]
        if isinstance(_observational_model, Unset):
            observational_model = UNSET
        else:
            observational_model = ObservationalModel(_observational_model)

        _time_perspective = d.pop("timePerspective", UNSET)
        time_perspective: Union[Unset, DesignTimePerspective]
        if isinstance(_time_perspective, Unset):
            time_perspective = UNSET
        else:
            time_perspective = DesignTimePerspective(_time_perspective)

        _masking_info = d.pop("maskingInfo", UNSET)
        masking_info: Union[Unset, MaskingBlock]
        if isinstance(_masking_info, Unset):
            masking_info = UNSET
        else:
            masking_info = MaskingBlock.from_dict(_masking_info)

        design_info = cls(
            allocation=allocation,
            intervention_model=intervention_model,
            intervention_model_description=intervention_model_description,
            primary_purpose=primary_purpose,
            observational_model=observational_model,
            time_perspective=time_perspective,
            masking_info=masking_info,
        )

        design_info.additional_properties = d
        return design_info

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
