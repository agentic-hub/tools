from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GotifyCredentials

class GotifyGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    operation: Optional[str] = Field(None, description="Operation")


class GotifyGetallTool(BaseTool):
    name: str = "gotify_getall"
    description: str = "Tool for gotify getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GotifyGetallToolInput
    credentials: Optional[GotifyCredentials] = None
