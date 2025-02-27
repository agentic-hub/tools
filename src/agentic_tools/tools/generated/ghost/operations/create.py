from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GhostCredentials

class GhostCreateToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the post to create")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Admin API")
    post_id: Optional[str] = Field(None, description="The ID of the post to delete")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    title: Optional[str] = Field(None, description="Post's title")
    content_format: Optional[str] = Field(None, description="The format of the post")
    operation: Optional[str] = Field(None, description="Operation")


class GhostCreateTool(BaseTool):
    name: str = "ghost_create"
    description: str = "Tool for ghost create operation - create operation"
    args_schema: type[BaseModel] | None = GhostCreateToolInput
    credentials: Optional[GhostCredentials] = None
