from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SpotifyCredentials

class SpotifyGetalbumsToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The artist's Spotify URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class SpotifyGetalbumsTool(BaseTool):
    name: str = "spotify_getalbums"
    description: str = "Tool for spotify getAlbums operation - getAlbums operation"
    args_schema: type[BaseModel] | None = SpotifyGetalbumsToolInput
    credentials: Optional[SpotifyCredentials] = None
