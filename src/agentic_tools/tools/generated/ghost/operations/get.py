from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GhostCredentials

class GhostGetToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the post to create")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Admin API")
    post_id: Optional[str] = Field(None, description="The ID of the post to delete")
    resource: Optional[str] = Field(None, description="Resource")
    by: Optional[str] = Field(None, description="Get the post either by slug or ID")
    identifier: Optional[str] = Field(None, description="The ID or slug of the post to get")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    content_format: Optional[str] = Field(None, description="The format of the post")
    operation: Optional[str] = Field(None, description="Operation")


class GhostGetTool(BaseTool):
    name: str = "ghost_get"
    description: str = "Tool for ghost get operation - get operation"
    args_schema: type[BaseModel] | None = GhostGetToolInput
    credentials: Optional[GhostCredentials] = None
