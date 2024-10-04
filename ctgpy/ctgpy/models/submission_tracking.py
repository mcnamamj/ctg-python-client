import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.first_mcp_info import FirstMcpInfo
    from ..models.submission_info import SubmissionInfo


T = TypeVar("T", bound="SubmissionTracking")


@_attrs_define
class SubmissionTracking:
    """
    Attributes:
        estimated_results_first_submit_date (Union[Unset, datetime.date]):
        first_mcp_info (Union[Unset, FirstMcpInfo]):
        submission_infos (Union[Unset, List['SubmissionInfo']]):
    """

    estimated_results_first_submit_date: Union[Unset, datetime.date] = UNSET
    first_mcp_info: Union[Unset, "FirstMcpInfo"] = UNSET
    submission_infos: Union[Unset, List["SubmissionInfo"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        estimated_results_first_submit_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_results_first_submit_date, Unset):
            estimated_results_first_submit_date = self.estimated_results_first_submit_date.isoformat()

        first_mcp_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.first_mcp_info, Unset):
            first_mcp_info = self.first_mcp_info.to_dict()

        submission_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.submission_infos, Unset):
            submission_infos = []
            for submission_infos_item_data in self.submission_infos:
                submission_infos_item = submission_infos_item_data.to_dict()
                submission_infos.append(submission_infos_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if estimated_results_first_submit_date is not UNSET:
            field_dict["estimatedResultsFirstSubmitDate"] = estimated_results_first_submit_date
        if first_mcp_info is not UNSET:
            field_dict["firstMcpInfo"] = first_mcp_info
        if submission_infos is not UNSET:
            field_dict["submissionInfos"] = submission_infos

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.first_mcp_info import FirstMcpInfo
        from ..models.submission_info import SubmissionInfo

        d = src_dict.copy()
        _estimated_results_first_submit_date = d.pop("estimatedResultsFirstSubmitDate", UNSET)
        estimated_results_first_submit_date: Union[Unset, datetime.date]
        if isinstance(_estimated_results_first_submit_date, Unset):
            estimated_results_first_submit_date = UNSET
        else:
            estimated_results_first_submit_date = isoparse(_estimated_results_first_submit_date).date()

        _first_mcp_info = d.pop("firstMcpInfo", UNSET)
        first_mcp_info: Union[Unset, FirstMcpInfo]
        if isinstance(_first_mcp_info, Unset):
            first_mcp_info = UNSET
        else:
            first_mcp_info = FirstMcpInfo.from_dict(_first_mcp_info)

        submission_infos = []
        _submission_infos = d.pop("submissionInfos", UNSET)
        for submission_infos_item_data in _submission_infos or []:
            submission_infos_item = SubmissionInfo.from_dict(submission_infos_item_data)

            submission_infos.append(submission_infos_item)

        submission_tracking = cls(
            estimated_results_first_submit_date=estimated_results_first_submit_date,
            first_mcp_info=first_mcp_info,
            submission_infos=submission_infos,
        )

        submission_tracking.additional_properties = d
        return submission_tracking

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
