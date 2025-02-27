from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SpotifyCredentials

class SpotifyNextsongToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The artist's Spotify URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class SpotifyNextsongTool(BaseTool):
    name: str = "spotify_nextsong"
    connector_id: str = "nodes-base.spotify"
    description: str = "Tool for spotify nextSong operation - nextSong operation"
    args_schema: type[BaseModel] | None = SpotifyNextsongToolInput
    credentials: Optional[SpotifyCredentials] = None
