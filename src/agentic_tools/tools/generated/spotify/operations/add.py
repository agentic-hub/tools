from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SpotifyCredentials

class SpotifyAddToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    track_id: Optional[str] = Field(None, description="The track's Spotify URI or its ID. The track to add/delete from the playlist.")
    id: Optional[str] = Field(None, description="The artist's Spotify URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class SpotifyAddTool(BaseTool):
    name: str = "spotify_add"
    description: str = "Tool for spotify add operation - add operation"
    args_schema: type[BaseModel] | None = SpotifyAddToolInput
    credentials: Optional[SpotifyCredentials] = None
