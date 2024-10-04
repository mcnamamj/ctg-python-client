from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.measurement import Measurement


T = TypeVar("T", bound="MeasureCategory")


@_attrs_define
class MeasureCategory:
    """
    Attributes:
        title (Union[Unset, str]):
        measurements (Union[Unset, List['Measurement']]):
    """

    title: Union[Unset, str] = UNSET
    measurements: Union[Unset, List["Measurement"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        measurements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.measurements, Unset):
            measurements = []
            for measurements_item_data in self.measurements:
                measurements_item = measurements_item_data.to_dict()
                measurements.append(measurements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if measurements is not UNSET:
            field_dict["measurements"] = measurements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.measurement import Measurement

        d = src_dict.copy()
        title = d.pop("title", UNSET)

        measurements = []
        _measurements = d.pop("measurements", UNSET)
        for measurements_item_data in _measurements or []:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        measure_category = cls(
            title=title,
            measurements=measurements,
        )

        measure_category.additional_properties = d
        return measure_category

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
