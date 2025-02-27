from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SpotifyCredentials

class SpotifyCreateToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    name: Optional[str] = Field(None, description="Name of the playlist to create")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The artist's Spotify URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class SpotifyCreateTool(BaseTool):
    name: str = "spotify_create"
    description: str = "Tool for spotify create operation - create operation"
    args_schema: type[BaseModel] | None = SpotifyCreateToolInput
    credentials: Optional[SpotifyCredentials] = None
