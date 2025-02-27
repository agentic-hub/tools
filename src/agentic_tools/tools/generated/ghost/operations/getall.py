from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GhostCredentials

class GhostGetallToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the post to create")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Admin API")
    post_id: Optional[str] = Field(None, description="The ID of the post to delete")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    content_format: Optional[str] = Field(None, description="The format of the post")
    operation: Optional[str] = Field(None, description="Operation")


class GhostGetallTool(BaseTool):
    name: str = "ghost_getall"
    connector_id: str = "nodes-base.ghost"
    description: str = "Tool for ghost getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GhostGetallToolInput
    credentials: Optional[GhostCredentials] = None
