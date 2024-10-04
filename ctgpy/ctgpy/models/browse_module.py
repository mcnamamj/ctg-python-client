from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.browse_branch import BrowseBranch
    from ..models.browse_leaf import BrowseLeaf
    from ..models.mesh import Mesh


T = TypeVar("T", bound="BrowseModule")


@_attrs_define
class BrowseModule:
    """
    Attributes:
        meshes (Union[Unset, List['Mesh']]):
        ancestors (Union[Unset, List['Mesh']]):
        browse_leaves (Union[Unset, List['BrowseLeaf']]):
        browse_branches (Union[Unset, List['BrowseBranch']]):
    """

    meshes: Union[Unset, List["Mesh"]] = UNSET
    ancestors: Union[Unset, List["Mesh"]] = UNSET
    browse_leaves: Union[Unset, List["BrowseLeaf"]] = UNSET
    browse_branches: Union[Unset, List["BrowseBranch"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meshes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.meshes, Unset):
            meshes = []
            for meshes_item_data in self.meshes:
                meshes_item = meshes_item_data.to_dict()
                meshes.append(meshes_item)

        ancestors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.ancestors, Unset):
            ancestors = []
            for ancestors_item_data in self.ancestors:
                ancestors_item = ancestors_item_data.to_dict()
                ancestors.append(ancestors_item)

        browse_leaves: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.browse_leaves, Unset):
            browse_leaves = []
            for browse_leaves_item_data in self.browse_leaves:
                browse_leaves_item = browse_leaves_item_data.to_dict()
                browse_leaves.append(browse_leaves_item)

        browse_branches: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.browse_branches, Unset):
            browse_branches = []
            for browse_branches_item_data in self.browse_branches:
                browse_branches_item = browse_branches_item_data.to_dict()
                browse_branches.append(browse_branches_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meshes is not UNSET:
            field_dict["meshes"] = meshes
        if ancestors is not UNSET:
            field_dict["ancestors"] = ancestors
        if browse_leaves is not UNSET:
            field_dict["browseLeaves"] = browse_leaves
        if browse_branches is not UNSET:
            field_dict["browseBranches"] = browse_branches

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.browse_branch import BrowseBranch
        from ..models.browse_leaf import BrowseLeaf
        from ..models.mesh import Mesh

        d = src_dict.copy()
        meshes = []
        _meshes = d.pop("meshes", UNSET)
        for meshes_item_data in _meshes or []:
            meshes_item = Mesh.from_dict(meshes_item_data)

            meshes.append(meshes_item)

        ancestors = []
        _ancestors = d.pop("ancestors", UNSET)
        for ancestors_item_data in _ancestors or []:
            ancestors_item = Mesh.from_dict(ancestors_item_data)

            ancestors.append(ancestors_item)

        browse_leaves = []
        _browse_leaves = d.pop("browseLeaves", UNSET)
        for browse_leaves_item_data in _browse_leaves or []:
            browse_leaves_item = BrowseLeaf.from_dict(browse_leaves_item_data)

            browse_leaves.append(browse_leaves_item)

        browse_branches = []
        _browse_branches = d.pop("browseBranches", UNSET)
        for browse_branches_item_data in _browse_branches or []:
            browse_branches_item = BrowseBranch.from_dict(browse_branches_item_data)

            browse_branches.append(browse_branches_item)

        browse_module = cls(
            meshes=meshes,
            ancestors=ancestors,
            browse_leaves=browse_leaves,
            browse_branches=browse_branches,
        )

        browse_module.additional_properties = d
        return browse_module

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
