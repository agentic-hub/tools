from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZoomCredentials

class ZoomGetToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    meeting_id: Optional[str] = Field(None, description="Meeting ID")
    operation: Optional[str] = Field(None, description="Operation")


class ZoomGetTool(BaseTool):
    name: str = "zoom_get"
    connector_id: str = "nodes-base.zoom"
    description: str = "Tool for zoom get operation - get operation"
    args_schema: type[BaseModel] | None = ZoomGetToolInput
    credentials: Optional[ZoomCredentials] = None
