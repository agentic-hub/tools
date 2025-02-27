from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZoomCredentials

class ZoomGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    meeting_id: Optional[str] = Field(None, description="Meeting ID")
    operation: Optional[str] = Field(None, description="Operation")


class ZoomGetallTool(BaseTool):
    name: str = "zoom_getall"
    description: str = "Tool for zoom getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = ZoomGetallToolInput
    credentials: Optional[ZoomCredentials] = None
