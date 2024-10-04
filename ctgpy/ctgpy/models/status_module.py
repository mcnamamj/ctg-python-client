import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_struct import DateStruct
    from ..models.expanded_access_info import ExpandedAccessInfo
    from ..models.partial_date_struct import PartialDateStruct


T = TypeVar("T", bound="StatusModule")


@_attrs_define
class StatusModule:
    """
    Attributes:
        status_verified_date (Union[Unset, str]): Date in `yyyy`, `yyyy-MM`, or `yyyy-MM-dd` format
        overall_status (Union[Unset, Status]):
        last_known_status (Union[Unset, Status]):
        delayed_posting (Union[Unset, bool]):
        why_stopped (Union[Unset, str]):
        expanded_access_info (Union[Unset, ExpandedAccessInfo]):
        start_date_struct (Union[Unset, PartialDateStruct]):
        primary_completion_date_struct (Union[Unset, PartialDateStruct]):
        completion_date_struct (Union[Unset, PartialDateStruct]):
        study_first_submit_date (Union[Unset, datetime.date]):
        study_first_submit_qc_date (Union[Unset, datetime.date]):
        study_first_post_date_struct (Union[Unset, DateStruct]):
        results_first_submit_date (Union[Unset, datetime.date]):
        results_first_submit_qc_date (Union[Unset, datetime.date]):
        results_first_post_date_struct (Union[Unset, DateStruct]):
        disp_first_submit_date (Union[Unset, datetime.date]):
        disp_first_submit_qc_date (Union[Unset, datetime.date]):
        disp_first_post_date_struct (Union[Unset, DateStruct]):
        last_update_submit_date (Union[Unset, datetime.date]):
        last_update_post_date_struct (Union[Unset, DateStruct]):
    """

    status_verified_date: Union[Unset, str] = UNSET
    overall_status: Union[Unset, Status] = UNSET
    last_known_status: Union[Unset, Status] = UNSET
    delayed_posting: Union[Unset, bool] = UNSET
    why_stopped: Union[Unset, str] = UNSET
    expanded_access_info: Union[Unset, "ExpandedAccessInfo"] = UNSET
    start_date_struct: Union[Unset, "PartialDateStruct"] = UNSET
    primary_completion_date_struct: Union[Unset, "PartialDateStruct"] = UNSET
    completion_date_struct: Union[Unset, "PartialDateStruct"] = UNSET
    study_first_submit_date: Union[Unset, datetime.date] = UNSET
    study_first_submit_qc_date: Union[Unset, datetime.date] = UNSET
    study_first_post_date_struct: Union[Unset, "DateStruct"] = UNSET
    results_first_submit_date: Union[Unset, datetime.date] = UNSET
    results_first_submit_qc_date: Union[Unset, datetime.date] = UNSET
    results_first_post_date_struct: Union[Unset, "DateStruct"] = UNSET
    disp_first_submit_date: Union[Unset, datetime.date] = UNSET
    disp_first_submit_qc_date: Union[Unset, datetime.date] = UNSET
    disp_first_post_date_struct: Union[Unset, "DateStruct"] = UNSET
    last_update_submit_date: Union[Unset, datetime.date] = UNSET
    last_update_post_date_struct: Union[Unset, "DateStruct"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        status_verified_date = self.status_verified_date

        overall_status: Union[Unset, str] = UNSET
        if not isinstance(self.overall_status, Unset):
            overall_status = self.overall_status.value

        last_known_status: Union[Unset, str] = UNSET
        if not isinstance(self.last_known_status, Unset):
            last_known_status = self.last_known_status.value

        delayed_posting = self.delayed_posting

        why_stopped = self.why_stopped

        expanded_access_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expanded_access_info, Unset):
            expanded_access_info = self.expanded_access_info.to_dict()

        start_date_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start_date_struct, Unset):
            start_date_struct = self.start_date_struct.to_dict()

        primary_completion_date_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.primary_completion_date_struct, Unset):
            primary_completion_date_struct = self.primary_completion_date_struct.to_dict()

        completion_date_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.completion_date_struct, Unset):
            completion_date_struct = self.completion_date_struct.to_dict()

        study_first_submit_date: Union[Unset, str] = UNSET
        if not isinstance(self.study_first_submit_date, Unset):
            study_first_submit_date = self.study_first_submit_date.isoformat()

        study_first_submit_qc_date: Union[Unset, str] = UNSET
        if not isinstance(self.study_first_submit_qc_date, Unset):
            study_first_submit_qc_date = self.study_first_submit_qc_date.isoformat()

        study_first_post_date_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.study_first_post_date_struct, Unset):
            study_first_post_date_struct = self.study_first_post_date_struct.to_dict()

        results_first_submit_date: Union[Unset, str] = UNSET
        if not isinstance(self.results_first_submit_date, Unset):
            results_first_submit_date = self.results_first_submit_date.isoformat()

        results_first_submit_qc_date: Union[Unset, str] = UNSET
        if not isinstance(self.results_first_submit_qc_date, Unset):
            results_first_submit_qc_date = self.results_first_submit_qc_date.isoformat()

        results_first_post_date_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.results_first_post_date_struct, Unset):
            results_first_post_date_struct = self.results_first_post_date_struct.to_dict()

        disp_first_submit_date: Union[Unset, str] = UNSET
        if not isinstance(self.disp_first_submit_date, Unset):
            disp_first_submit_date = self.disp_first_submit_date.isoformat()

        disp_first_submit_qc_date: Union[Unset, str] = UNSET
        if not isinstance(self.disp_first_submit_qc_date, Unset):
            disp_first_submit_qc_date = self.disp_first_submit_qc_date.isoformat()

        disp_first_post_date_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disp_first_post_date_struct, Unset):
            disp_first_post_date_struct = self.disp_first_post_date_struct.to_dict()

        last_update_submit_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_submit_date, Unset):
            last_update_submit_date = self.last_update_submit_date.isoformat()

        last_update_post_date_struct: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_update_post_date_struct, Unset):
            last_update_post_date_struct = self.last_update_post_date_struct.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status_verified_date is not UNSET:
            field_dict["statusVerifiedDate"] = status_verified_date
        if overall_status is not UNSET:
            field_dict["overallStatus"] = overall_status
        if last_known_status is not UNSET:
            field_dict["lastKnownStatus"] = last_known_status
        if delayed_posting is not UNSET:
            field_dict["delayedPosting"] = delayed_posting
        if why_stopped is not UNSET:
            field_dict["whyStopped"] = why_stopped
        if expanded_access_info is not UNSET:
            field_dict["expandedAccessInfo"] = expanded_access_info
        if start_date_struct is not UNSET:
            field_dict["startDateStruct"] = start_date_struct
        if primary_completion_date_struct is not UNSET:
            field_dict["primaryCompletionDateStruct"] = primary_completion_date_struct
        if completion_date_struct is not UNSET:
            field_dict["completionDateStruct"] = completion_date_struct
        if study_first_submit_date is not UNSET:
            field_dict["studyFirstSubmitDate"] = study_first_submit_date
        if study_first_submit_qc_date is not UNSET:
            field_dict["studyFirstSubmitQcDate"] = study_first_submit_qc_date
        if study_first_post_date_struct is not UNSET:
            field_dict["studyFirstPostDateStruct"] = study_first_post_date_struct
        if results_first_submit_date is not UNSET:
            field_dict["resultsFirstSubmitDate"] = results_first_submit_date
        if results_first_submit_qc_date is not UNSET:
            field_dict["resultsFirstSubmitQcDate"] = results_first_submit_qc_date
        if results_first_post_date_struct is not UNSET:
            field_dict["resultsFirstPostDateStruct"] = results_first_post_date_struct
        if disp_first_submit_date is not UNSET:
            field_dict["dispFirstSubmitDate"] = disp_first_submit_date
        if disp_first_submit_qc_date is not UNSET:
            field_dict["dispFirstSubmitQcDate"] = disp_first_submit_qc_date
        if disp_first_post_date_struct is not UNSET:
            field_dict["dispFirstPostDateStruct"] = disp_first_post_date_struct
        if last_update_submit_date is not UNSET:
            field_dict["lastUpdateSubmitDate"] = last_update_submit_date
        if last_update_post_date_struct is not UNSET:
            field_dict["lastUpdatePostDateStruct"] = last_update_post_date_struct

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.date_struct import DateStruct
        from ..models.expanded_access_info import ExpandedAccessInfo
        from ..models.partial_date_struct import PartialDateStruct

        d = src_dict.copy()
        status_verified_date = d.pop("statusVerifiedDate", UNSET)

        _overall_status = d.pop("overallStatus", UNSET)
        overall_status: Union[Unset, Status]
        if isinstance(_overall_status, Unset):
            overall_status = UNSET
        else:
            overall_status = Status(_overall_status)

        _last_known_status = d.pop("lastKnownStatus", UNSET)
        last_known_status: Union[Unset, Status]
        if isinstance(_last_known_status, Unset):
            last_known_status = UNSET
        else:
            last_known_status = Status(_last_known_status)

        delayed_posting = d.pop("delayedPosting", UNSET)

        why_stopped = d.pop("whyStopped", UNSET)

        _expanded_access_info = d.pop("expandedAccessInfo", UNSET)
        expanded_access_info: Union[Unset, ExpandedAccessInfo]
        if isinstance(_expanded_access_info, Unset):
            expanded_access_info = UNSET
        else:
            expanded_access_info = ExpandedAccessInfo.from_dict(_expanded_access_info)

        _start_date_struct = d.pop("startDateStruct", UNSET)
        start_date_struct: Union[Unset, PartialDateStruct]
        if isinstance(_start_date_struct, Unset):
            start_date_struct = UNSET
        else:
            start_date_struct = PartialDateStruct.from_dict(_start_date_struct)

        _primary_completion_date_struct = d.pop("primaryCompletionDateStruct", UNSET)
        primary_completion_date_struct: Union[Unset, PartialDateStruct]
        if isinstance(_primary_completion_date_struct, Unset):
            primary_completion_date_struct = UNSET
        else:
            primary_completion_date_struct = PartialDateStruct.from_dict(_primary_completion_date_struct)

        _completion_date_struct = d.pop("completionDateStruct", UNSET)
        completion_date_struct: Union[Unset, PartialDateStruct]
        if isinstance(_completion_date_struct, Unset):
            completion_date_struct = UNSET
        else:
            completion_date_struct = PartialDateStruct.from_dict(_completion_date_struct)

        _study_first_submit_date = d.pop("studyFirstSubmitDate", UNSET)
        study_first_submit_date: Union[Unset, datetime.date]
        if isinstance(_study_first_submit_date, Unset):
            study_first_submit_date = UNSET
        else:
            study_first_submit_date = isoparse(_study_first_submit_date).date()

        _study_first_submit_qc_date = d.pop("studyFirstSubmitQcDate", UNSET)
        study_first_submit_qc_date: Union[Unset, datetime.date]
        if isinstance(_study_first_submit_qc_date, Unset):
            study_first_submit_qc_date = UNSET
        else:
            study_first_submit_qc_date = isoparse(_study_first_submit_qc_date).date()

        _study_first_post_date_struct = d.pop("studyFirstPostDateStruct", UNSET)
        study_first_post_date_struct: Union[Unset, DateStruct]
        if isinstance(_study_first_post_date_struct, Unset):
            study_first_post_date_struct = UNSET
        else:
            study_first_post_date_struct = DateStruct.from_dict(_study_first_post_date_struct)

        _results_first_submit_date = d.pop("resultsFirstSubmitDate", UNSET)
        results_first_submit_date: Union[Unset, datetime.date]
        if isinstance(_results_first_submit_date, Unset):
            results_first_submit_date = UNSET
        else:
            results_first_submit_date = isoparse(_results_first_submit_date).date()

        _results_first_submit_qc_date = d.pop("resultsFirstSubmitQcDate", UNSET)
        results_first_submit_qc_date: Union[Unset, datetime.date]
        if isinstance(_results_first_submit_qc_date, Unset):
            results_first_submit_qc_date = UNSET
        else:
            results_first_submit_qc_date = isoparse(_results_first_submit_qc_date).date()

        _results_first_post_date_struct = d.pop("resultsFirstPostDateStruct", UNSET)
        results_first_post_date_struct: Union[Unset, DateStruct]
        if isinstance(_results_first_post_date_struct, Unset):
            results_first_post_date_struct = UNSET
        else:
            results_first_post_date_struct = DateStruct.from_dict(_results_first_post_date_struct)

        _disp_first_submit_date = d.pop("dispFirstSubmitDate", UNSET)
        disp_first_submit_date: Union[Unset, datetime.date]
        if isinstance(_disp_first_submit_date, Unset):
            disp_first_submit_date = UNSET
        else:
            disp_first_submit_date = isoparse(_disp_first_submit_date).date()

        _disp_first_submit_qc_date = d.pop("dispFirstSubmitQcDate", UNSET)
        disp_first_submit_qc_date: Union[Unset, datetime.date]
        if isinstance(_disp_first_submit_qc_date, Unset):
            disp_first_submit_qc_date = UNSET
        else:
            disp_first_submit_qc_date = isoparse(_disp_first_submit_qc_date).date()

        _disp_first_post_date_struct = d.pop("dispFirstPostDateStruct", UNSET)
        disp_first_post_date_struct: Union[Unset, DateStruct]
        if isinstance(_disp_first_post_date_struct, Unset):
            disp_first_post_date_struct = UNSET
        else:
            disp_first_post_date_struct = DateStruct.from_dict(_disp_first_post_date_struct)

        _last_update_submit_date = d.pop("lastUpdateSubmitDate", UNSET)
        last_update_submit_date: Union[Unset, datetime.date]
        if isinstance(_last_update_submit_date, Unset):
            last_update_submit_date = UNSET
        else:
            last_update_submit_date = isoparse(_last_update_submit_date).date()

        _last_update_post_date_struct = d.pop("lastUpdatePostDateStruct", UNSET)
        last_update_post_date_struct: Union[Unset, DateStruct]
        if isinstance(_last_update_post_date_struct, Unset):
            last_update_post_date_struct = UNSET
        else:
            last_update_post_date_struct = DateStruct.from_dict(_last_update_post_date_struct)

        status_module = cls(
            status_verified_date=status_verified_date,
            overall_status=overall_status,
            last_known_status=last_known_status,
            delayed_posting=delayed_posting,
            why_stopped=why_stopped,
            expanded_access_info=expanded_access_info,
            start_date_struct=start_date_struct,
            primary_completion_date_struct=primary_completion_date_struct,
            completion_date_struct=completion_date_struct,
            study_first_submit_date=study_first_submit_date,
            study_first_submit_qc_date=study_first_submit_qc_date,
            study_first_post_date_struct=study_first_post_date_struct,
            results_first_submit_date=results_first_submit_date,
            results_first_submit_qc_date=results_first_submit_qc_date,
            results_first_post_date_struct=results_first_post_date_struct,
            disp_first_submit_date=disp_first_submit_date,
            disp_first_submit_qc_date=disp_first_submit_qc_date,
            disp_first_post_date_struct=disp_first_post_date_struct,
            last_update_submit_date=last_update_submit_date,
            last_update_post_date_struct=last_update_post_date_struct,
        )

        status_module.additional_properties = d
        return status_module

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
