from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZoomCredentials

class Zoom__custom_api_call__ToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    meeting_id: Optional[str] = Field(None, description="Meeting ID")
    operation: Optional[str] = Field(None, description="Operation")


class Zoom__custom_api_call__Tool(BaseTool):
    name: str = "zoom___custom_api_call__"
    connector_id: str = "nodes-base.zoom"
    description: str = "Tool for zoom __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Zoom__custom_api_call__ToolInput
    credentials: Optional[ZoomCredentials] = None
