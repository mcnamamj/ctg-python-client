from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drop_withdraw import DropWithdraw
    from ..models.flow_milestone import FlowMilestone


T = TypeVar("T", bound="FlowPeriod")


@_attrs_define
class FlowPeriod:
    """
    Attributes:
        title (Union[Unset, str]):
        milestones (Union[Unset, List['FlowMilestone']]):
        drop_withdraws (Union[Unset, List['DropWithdraw']]):
    """

    title: Union[Unset, str] = UNSET
    milestones: Union[Unset, List["FlowMilestone"]] = UNSET
    drop_withdraws: Union[Unset, List["DropWithdraw"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        milestones: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.milestones, Unset):
            milestones = []
            for milestones_item_data in self.milestones:
                milestones_item = milestones_item_data.to_dict()
                milestones.append(milestones_item)

        drop_withdraws: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.drop_withdraws, Unset):
            drop_withdraws = []
            for drop_withdraws_item_data in self.drop_withdraws:
                drop_withdraws_item = drop_withdraws_item_data.to_dict()
                drop_withdraws.append(drop_withdraws_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if milestones is not UNSET:
            field_dict["milestones"] = milestones
        if drop_withdraws is not UNSET:
            field_dict["dropWithdraws"] = drop_withdraws

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.drop_withdraw import DropWithdraw
        from ..models.flow_milestone import FlowMilestone

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        milestones = []
        _milestones = d.pop("milestones", UNSET)
        for milestones_item_data in _milestones or []:
            milestones_item = FlowMilestone.from_dict(milestones_item_data)

            milestones.append(milestones_item)

        drop_withdraws = []
        _drop_withdraws = d.pop("dropWithdraws", UNSET)
        for drop_withdraws_item_data in _drop_withdraws or []:
            drop_withdraws_item = DropWithdraw.from_dict(drop_withdraws_item_data)

            drop_withdraws.append(drop_withdraws_item)

        flow_period = cls(
            title=title,
            milestones=milestones,
            drop_withdraws=drop_withdraws,
        )

        flow_period.additional_properties = d
        return flow_period

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
