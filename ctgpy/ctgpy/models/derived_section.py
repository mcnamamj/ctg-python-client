from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.browse_module import BrowseModule
    from ..models.misc_info_module import MiscInfoModule


T = TypeVar("T", bound="DerivedSection")


@_attrs_define
class DerivedSection:
    """
    Attributes:
        misc_info_module (Union[Unset, MiscInfoModule]):
        condition_browse_module (Union[Unset, BrowseModule]):
        intervention_browse_module (Union[Unset, BrowseModule]):
    """

    misc_info_module: Union[Unset, "MiscInfoModule"] = UNSET
    condition_browse_module: Union[Unset, "BrowseModule"] = UNSET
    intervention_browse_module: Union[Unset, "BrowseModule"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        misc_info_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.misc_info_module, Unset):
            misc_info_module = self.misc_info_module.to_dict()

        condition_browse_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.condition_browse_module, Unset):
            condition_browse_module = self.condition_browse_module.to_dict()

        intervention_browse_module: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.intervention_browse_module, Unset):
            intervention_browse_module = self.intervention_browse_module.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if misc_info_module is not UNSET:
            field_dict["miscInfoModule"] = misc_info_module
        if condition_browse_module is not UNSET:
            field_dict["conditionBrowseModule"] = condition_browse_module
        if intervention_browse_module is not UNSET:
            field_dict["interventionBrowseModule"] = intervention_browse_module

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.browse_module import BrowseModule
        from ..models.misc_info_module import MiscInfoModule

        d = src_dict.copy()
        _misc_info_module = d.pop("miscInfoModule", UNSET)
        misc_info_module: Union[Unset, MiscInfoModule]
        if isinstance(_misc_info_module, Unset):
            misc_info_module = UNSET
        else:
            misc_info_module = MiscInfoModule.from_dict(_misc_info_module)

        _condition_browse_module = d.pop("conditionBrowseModule", UNSET)
        condition_browse_module: Union[Unset, BrowseModule]
        if isinstance(_condition_browse_module, Unset):
            condition_browse_module = UNSET
        else:
            condition_browse_module = BrowseModule.from_dict(_condition_browse_module)

        _intervention_browse_module = d.pop("interventionBrowseModule", UNSET)
        intervention_browse_module: Union[Unset, BrowseModule]
        if isinstance(_intervention_browse_module, Unset):
            intervention_browse_module = UNSET
        else:
            intervention_browse_module = BrowseModule.from_dict(_intervention_browse_module)

        derived_section = cls(
            misc_info_module=misc_info_module,
            condition_browse_module=condition_browse_module,
            intervention_browse_module=intervention_browse_module,
        )

        derived_section.additional_properties = d
        return derived_section

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
