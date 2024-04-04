from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dist_item import DistItem
    from ..models.gzip_stats_percentiles import GzipStatsPercentiles
    from ..models.study_size import StudySize


T = TypeVar("T", bound="GzipStats")


@_attrs_define
class GzipStats:
    """
    Attributes:
        average_size_bytes (int):
        largest_studies (List['StudySize']):
        percentiles (GzipStatsPercentiles):
        ranges (List['DistItem']):
        total_studies (int):
    """

    average_size_bytes: int
    largest_studies: List["StudySize"]
    percentiles: "GzipStatsPercentiles"
    ranges: List["DistItem"]
    total_studies: int

    def to_dict(self) -> Dict[str, Any]:
        average_size_bytes = self.average_size_bytes

        largest_studies = []
        for largest_studies_item_data in self.largest_studies:
            largest_studies_item = largest_studies_item_data.to_dict()
            largest_studies.append(largest_studies_item)

        percentiles = self.percentiles.to_dict()

        ranges = []
        for ranges_item_data in self.ranges:
            ranges_item = ranges_item_data.to_dict()
            ranges.append(ranges_item)

        total_studies = self.total_studies

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "averageSizeBytes": average_size_bytes,
                "largestStudies": largest_studies,
                "percentiles": percentiles,
                "ranges": ranges,
                "totalStudies": total_studies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.dist_item import DistItem
        from ..models.gzip_stats_percentiles import GzipStatsPercentiles
        from ..models.study_size import StudySize

        d = src_dict.copy()
        average_size_bytes = d.pop("averageSizeBytes")

        largest_studies = []
        _largest_studies = d.pop("largestStudies")
        for largest_studies_item_data in _largest_studies:
            largest_studies_item = StudySize.from_dict(largest_studies_item_data)

            largest_studies.append(largest_studies_item)

        percentiles = GzipStatsPercentiles.from_dict(d.pop("percentiles"))

        ranges = []
        _ranges = d.pop("ranges")
        for ranges_item_data in _ranges:
            ranges_item = DistItem.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        total_studies = d.pop("totalStudies")

        gzip_stats = cls(
            average_size_bytes=average_size_bytes,
            largest_studies=largest_studies,
            percentiles=percentiles,
            ranges=ranges,
            total_studies=total_studies,
        )

        return gzip_stats
