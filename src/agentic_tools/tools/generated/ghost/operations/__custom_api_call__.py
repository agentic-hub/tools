from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GhostCredentials

class Ghost__custom_api_call__ToolInput(BaseModel):
    content: Optional[str] = Field(None, description="The content of the post to create")
    source: Optional[str] = Field(None, description="Pick where your data comes from, Content or Admin API")
    post_id: Optional[str] = Field(None, description="The ID of the post to delete")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    content_format: Optional[str] = Field(None, description="The format of the post")
    operation: Optional[str] = Field(None, description="Operation")


class Ghost__custom_api_call__Tool(BaseTool):
    name: str = "ghost___custom_api_call__"
    description: str = "Tool for ghost __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Ghost__custom_api_call__ToolInput
    credentials: Optional[GhostCredentials] = None
