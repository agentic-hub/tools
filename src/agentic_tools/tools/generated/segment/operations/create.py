from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SegmentCredentials

class SegmentCreateToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="User ID")
    resource: Optional[str] = Field(None, description="Resource")
    context: Optional[Dict[str, Any]] = Field(None, description="Context")
    integrations: Optional[Dict[str, Any]] = Field(None, description="Integration")
    traits: Optional[Dict[str, Any]] = Field(None, description="Traits")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class SegmentCreateTool(BaseTool):
    name: str = "segment_create"
    connector_id: str = "nodes-base.segment"
    description: str = "Tool for segment create operation - create operation"
    args_schema: type[BaseModel] | None = SegmentCreateToolInput
    credentials: Optional[SegmentCredentials] = None
