from pathlib import Path
from typing import Optional, Tuple

from ..model import TrackJson, ConfigJson, OnlineModule
from ..modifier import Result
from ..utils import Log


class Pull:
    _max_size: float

    _log: Log
    _local_folder: Path

    _config: ConfigJson

    modules_folder: Path

    def __init__(self, root_folder: Path, config: ConfigJson): ...
    @staticmethod
    def _copy_file(old: Path, new: Path, delete_old: bool = True): ...
    @staticmethod
    @Result.catching()
    def _safe_download(url: str, out: Path) -> Result: ...
    def _check_changelog(self, module_id: str, file: Path) -> bool: ...
    def _get_file_url(self, module_id: str, file: Path) -> str: ...
    def _get_changelog_common(self, module_id: str, changelog: str) -> Optional[Path]: ...
    def _from_zip_common(
        self, module_id: str, zip_file: Path, changelog_file: Optional[Path], *, delete_tmp: bool = ...
    ) -> Optional[OnlineModule]: ...
    def from_json(self, track: TrackJson, *, local: bool) -> Tuple[Optional[OnlineModule], float]: ...
    def from_url(self, track: TrackJson) -> Tuple[Optional[OnlineModule], float]: ...
    def from_git(self, track: TrackJson) -> Tuple[Optional[OnlineModule], float]: ...
    def from_zip(self, track: TrackJson) -> Tuple[Optional[OnlineModule], float]: ...
    def from_track(self, track: TrackJson) -> Tuple[Optional[OnlineModule], float]: ...
    @classmethod
    def set_max_size(cls, value: float): ...