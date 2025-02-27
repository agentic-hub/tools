from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SegmentCredentials

class SegmentEventToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="User ID")
    resource: Optional[str] = Field(None, description="Resource")
    context: Optional[Dict[str, Any]] = Field(None, description="Context")
    integrations: Optional[Dict[str, Any]] = Field(None, description="Integration")
    event: Optional[str] = Field(None, description="Name of the action that a user has performed")
    traits: Optional[Dict[str, Any]] = Field(None, description="Traits")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class SegmentEventTool(BaseTool):
    name: str = "segment_event"
    description: str = "Tool for segment event operation - event operation"
    args_schema: type[BaseModel] | None = SegmentEventToolInput
    credentials: Optional[SegmentCredentials] = None
