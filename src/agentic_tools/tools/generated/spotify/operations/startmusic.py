from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SpotifyCredentials

class SpotifyStartmusicToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="Enter a playlist, artist, or album URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class SpotifyStartmusicTool(BaseTool):
    name: str = "spotify_startmusic"
    description: str = "Tool for spotify startMusic operation - startMusic operation"
    args_schema: type[BaseModel] | None = SpotifyStartmusicToolInput
    credentials: Optional[SpotifyCredentials] = None
