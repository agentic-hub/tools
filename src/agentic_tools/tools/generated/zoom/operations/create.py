from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZoomCredentials

class ZoomCreateToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    meeting_id: Optional[str] = Field(None, description="Meeting ID")
    topic: Optional[str] = Field(None, description="Topic of the meeting")
    operation: Optional[str] = Field(None, description="Operation")


class ZoomCreateTool(BaseTool):
    name: str = "zoom_create"
    connector_id: str = "nodes-base.zoom"
    description: str = "Tool for zoom create operation - create operation"
    args_schema: type[BaseModel] | None = ZoomCreateToolInput
    credentials: Optional[ZoomCredentials] = None
