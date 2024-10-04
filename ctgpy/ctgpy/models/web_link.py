from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="WebLink")


@_attrs_define
class WebLink:
    """
    Attributes:
        label (str):
        url (str):
    """

    label: str
    url: str

    def to_dict(self) -> Dict[str, Any]:
        label = self.label

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "label": label,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        url = d.pop("url")

        web_link = cls(
            label=label,
            url=url,
        )

        return web_link
