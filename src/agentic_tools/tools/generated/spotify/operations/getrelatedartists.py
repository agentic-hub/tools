from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SpotifyCredentials

class SpotifyGetrelatedartistsToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The artist's Spotify URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class SpotifyGetrelatedartistsTool(BaseTool):
    name: str = "spotify_getrelatedartists"
    connector_id: str = "nodes-base.spotify"
    description: str = "Tool for spotify getRelatedArtists operation - getRelatedArtists operation"
    args_schema: type[BaseModel] | None = SpotifyGetrelatedartistsToolInput
    credentials: Optional[SpotifyCredentials] = None
