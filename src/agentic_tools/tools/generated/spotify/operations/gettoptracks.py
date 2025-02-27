from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SpotifyCredentials

class SpotifyGettoptracksToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    country: Optional[str] = Field(None, description="Top tracks in which country? Enter the postal abbreviation")
    id: Optional[str] = Field(None, description="The artist's Spotify URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class SpotifyGettoptracksTool(BaseTool):
    name: str = "spotify_gettoptracks"
    connector_id: str = "nodes-base.spotify"
    description: str = "Tool for spotify getTopTracks operation - getTopTracks operation"
    args_schema: type[BaseModel] | None = SpotifyGettoptracksToolInput
    credentials: Optional[SpotifyCredentials] = None
