from pathlib import Path
from typing import Optional

from .Pull import Pull
from ..model import ModulesJson, ConfigJson, TrackJson, OnlineModule
from ..track import BaseTracks
from ..utils import Log


class Sync:
    _log: Log
    _root_folder: Path
    _pull: Pull

    _json_folder: Path
    _modules_folder: Path
    _config: ConfigJson
    _tracks: BaseTracks

    timestamp: float
    modules_json: ModulesJson

    def  __init__(self, root_folder: Path, config: ConfigJson): ...
    def _update_jsons(self, track: TrackJson) -> Optional[OnlineModule]: ...
    def _check_tracks(self, obj: BaseTracks, cls: type): ...
    def create_github_tracks(self, api_token: str) -> BaseTracks: ...
    def create_local_tracks(self) -> BaseTracks: ...
    def create_tracks(self, **kwargs) -> BaseTracks: ...
    def update_by_id(self, module_id: str, **kwargs): ...
    def update_all(self, **kwargs): ...
    def write_modules_json(self): ...