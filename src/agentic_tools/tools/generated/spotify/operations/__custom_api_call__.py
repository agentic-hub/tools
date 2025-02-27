from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SpotifyCredentials

class Spotify__custom_api_call__ToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    id: Optional[str] = Field(None, description="The artist's Spotify URI or ID")
    query: Optional[str] = Field(None, description="The keyword term to search for")
    operation: Optional[str] = Field(None, description="Operation")


class Spotify__custom_api_call__Tool(BaseTool):
    name: str = "spotify___custom_api_call__"
    description: str = "Tool for spotify __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Spotify__custom_api_call__ToolInput
    credentials: Optional[SpotifyCredentials] = None
