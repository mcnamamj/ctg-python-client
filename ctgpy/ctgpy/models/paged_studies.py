from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.study import Study


T = TypeVar("T", bound="PagedStudies")


@_attrs_define
class PagedStudies:
    """
    Attributes:
        studies (List['Study']): `study` field values of type `markup` are in markdown format.
        next_page_token (Union[Unset, str]):
        total_count (Union[Unset, int]):
    """

    studies: List["Study"]
    next_page_token: Union[Unset, str] = UNSET
    total_count: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        studies = []
        for componentsschemas_study_list_item_data in self.studies:
            componentsschemas_study_list_item = componentsschemas_study_list_item_data.to_dict()
            studies.append(componentsschemas_study_list_item)

        next_page_token = self.next_page_token

        total_count = self.total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "studies": studies,
            }
        )
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.study import Study

        d = src_dict.copy()
        studies = []
        _studies = d.pop("studies")
        for componentsschemas_study_list_item_data in _studies:
            componentsschemas_study_list_item = Study.from_dict(componentsschemas_study_list_item_data)

            studies.append(componentsschemas_study_list_item)

        next_page_token = d.pop("nextPageToken", UNSET)

        total_count = d.pop("totalCount", UNSET)

        paged_studies = cls(
            studies=studies,
            next_page_token=next_page_token,
            total_count=total_count,
        )

        return paged_studies
