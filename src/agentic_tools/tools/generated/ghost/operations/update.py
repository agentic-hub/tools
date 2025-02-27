from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GhostCredentials

class GhostUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="The content of the post to create")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Admin API")
    post_id: Optional[str] = Field(None, description="The ID of the post to update")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    content_format: Optional[str] = Field(None, description="The format of the post")
    operation: Optional[str] = Field(None, description="Operation")


class GhostUpdateTool(BaseTool):
    name: str = "ghost_update"
    connector_id: str = "nodes-base.ghost"
    description: str = "Tool for ghost update operation - update operation"
    args_schema: type[BaseModel] | None = GhostUpdateToolInput
    credentials: Optional[GhostCredentials] = None
