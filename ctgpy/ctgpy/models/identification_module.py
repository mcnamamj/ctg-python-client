from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.org_study_id_info import OrgStudyIdInfo
    from ..models.organization import Organization
    from ..models.secondary_id_info import SecondaryIdInfo


T = TypeVar("T", bound="IdentificationModule")


@_attrs_define
class IdentificationModule:
    """
    Attributes:
        nct_id (Union[Unset, str]):
        nct_id_aliases (Union[Unset, List[str]]):
        org_study_id_info (Union[Unset, OrgStudyIdInfo]):
        secondary_id_infos (Union[Unset, List['SecondaryIdInfo']]):
        brief_title (Union[Unset, str]):
        official_title (Union[Unset, str]):
        acronym (Union[Unset, str]):
        organization (Union[Unset, Organization]):
    """

    nct_id: Union[Unset, str] = UNSET
    nct_id_aliases: Union[Unset, List[str]] = UNSET
    org_study_id_info: Union[Unset, "OrgStudyIdInfo"] = UNSET
    secondary_id_infos: Union[Unset, List["SecondaryIdInfo"]] = UNSET
    brief_title: Union[Unset, str] = UNSET
    official_title: Union[Unset, str] = UNSET
    acronym: Union[Unset, str] = UNSET
    organization: Union[Unset, "Organization"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nct_id = self.nct_id

        nct_id_aliases: Union[Unset, List[str]] = UNSET
        if not isinstance(self.nct_id_aliases, Unset):
            nct_id_aliases = self.nct_id_aliases

        org_study_id_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.org_study_id_info, Unset):
            org_study_id_info = self.org_study_id_info.to_dict()

        secondary_id_infos: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.secondary_id_infos, Unset):
            secondary_id_infos = []
            for secondary_id_infos_item_data in self.secondary_id_infos:
                secondary_id_infos_item = secondary_id_infos_item_data.to_dict()
                secondary_id_infos.append(secondary_id_infos_item)

        brief_title = self.brief_title

        official_title = self.official_title

        acronym = self.acronym

        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nct_id is not UNSET:
            field_dict["nctId"] = nct_id
        if nct_id_aliases is not UNSET:
            field_dict["nctIdAliases"] = nct_id_aliases
        if org_study_id_info is not UNSET:
            field_dict["orgStudyIdInfo"] = org_study_id_info
        if secondary_id_infos is not UNSET:
            field_dict["secondaryIdInfos"] = secondary_id_infos
        if brief_title is not UNSET:
            field_dict["briefTitle"] = brief_title
        if official_title is not UNSET:
            field_dict["officialTitle"] = official_title
        if acronym is not UNSET:
            field_dict["acronym"] = acronym
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.org_study_id_info import OrgStudyIdInfo
        from ..models.organization import Organization
        from ..models.secondary_id_info import SecondaryIdInfo

        d = src_dict.copy()
        nct_id = d.pop("nctId", UNSET)

        nct_id_aliases = cast(List[str], d.pop("nctIdAliases", UNSET))

        _org_study_id_info = d.pop("orgStudyIdInfo", UNSET)
        org_study_id_info: Union[Unset, OrgStudyIdInfo]
        if isinstance(_org_study_id_info, Unset):
            org_study_id_info = UNSET
        else:
            org_study_id_info = OrgStudyIdInfo.from_dict(_org_study_id_info)

        secondary_id_infos = []
        _secondary_id_infos = d.pop("secondaryIdInfos", UNSET)
        for secondary_id_infos_item_data in _secondary_id_infos or []:
            secondary_id_infos_item = SecondaryIdInfo.from_dict(secondary_id_infos_item_data)

            secondary_id_infos.append(secondary_id_infos_item)

        brief_title = d.pop("briefTitle", UNSET)

        official_title = d.pop("officialTitle", UNSET)

        acronym = d.pop("acronym", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, Organization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = Organization.from_dict(_organization)

        identification_module = cls(
            nct_id=nct_id,
            nct_id_aliases=nct_id_aliases,
            org_study_id_info=org_study_id_info,
            secondary_id_infos=secondary_id_infos,
            brief_title=brief_title,
            official_title=official_title,
            acronym=acronym,
            organization=organization,
        )

        identification_module.additional_properties = d
        return identification_module

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
