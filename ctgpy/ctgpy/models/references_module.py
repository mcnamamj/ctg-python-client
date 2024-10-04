from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.avail_ipd import AvailIpd
    from ..models.reference import Reference
    from ..models.see_also_link import SeeAlsoLink


T = TypeVar("T", bound="ReferencesModule")


@_attrs_define
class ReferencesModule:
    """
    Attributes:
        references (Union[Unset, List['Reference']]):
        see_also_links (Union[Unset, List['SeeAlsoLink']]):
        avail_ipds (Union[Unset, List['AvailIpd']]):
    """

    references: Union[Unset, List["Reference"]] = UNSET
    see_also_links: Union[Unset, List["SeeAlsoLink"]] = UNSET
    avail_ipds: Union[Unset, List["AvailIpd"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        references: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        see_also_links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.see_also_links, Unset):
            see_also_links = []
            for see_also_links_item_data in self.see_also_links:
                see_also_links_item = see_also_links_item_data.to_dict()
                see_also_links.append(see_also_links_item)

        avail_ipds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.avail_ipds, Unset):
            avail_ipds = []
            for avail_ipds_item_data in self.avail_ipds:
                avail_ipds_item = avail_ipds_item_data.to_dict()
                avail_ipds.append(avail_ipds_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if references is not UNSET:
            field_dict["references"] = references
        if see_also_links is not UNSET:
            field_dict["seeAlsoLinks"] = see_also_links
        if avail_ipds is not UNSET:
            field_dict["availIpds"] = avail_ipds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.avail_ipd import AvailIpd
        from ..models.reference import Reference
        from ..models.see_also_link import SeeAlsoLink

        d = src_dict.copy()
        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = Reference.from_dict(references_item_data)

            references.append(references_item)

        see_also_links = []
        _see_also_links = d.pop("seeAlsoLinks", UNSET)
        for see_also_links_item_data in _see_also_links or []:
            see_also_links_item = SeeAlsoLink.from_dict(see_also_links_item_data)

            see_also_links.append(see_also_links_item)

        avail_ipds = []
        _avail_ipds = d.pop("availIpds", UNSET)
        for avail_ipds_item_data in _avail_ipds or []:
            avail_ipds_item = AvailIpd.from_dict(avail_ipds_item_data)

            avail_ipds.append(avail_ipds_item)

        references_module = cls(
            references=references,
            see_also_links=see_also_links,
            avail_ipds=avail_ipds,
        )

        references_module.additional_properties = d
        return references_module

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
