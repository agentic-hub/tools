from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZoomCredentials

class ZoomUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    meeting_id: Optional[str] = Field(None, description="Meeting ID")
    operation: Optional[str] = Field(None, description="Operation")


class ZoomUpdateTool(BaseTool):
    name: str = "zoom_update"
    description: str = "Tool for zoom update operation - update operation"
    args_schema: type[BaseModel] | None = ZoomUpdateToolInput
    credentials: Optional[ZoomCredentials] = None
