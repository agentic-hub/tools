from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SegmentCredentials

class SegmentAddToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="User ID")
    resource: Optional[str] = Field(None, description="Resource")
    context: Optional[Dict[str, Any]] = Field(None, description="Context")
    integrations: Optional[Dict[str, Any]] = Field(None, description="Integration")
    traits: Optional[Dict[str, Any]] = Field(None, description="Traits")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    group_id: Optional[str] = Field(None, description="A Group ID is the unique identifier which you recognize a group by in your own database")
    operation: Optional[str] = Field(None, description="Operation")


class SegmentAddTool(BaseTool):
    name: str = "segment_add"
    description: str = "Tool for segment add operation - add operation"
    args_schema: type[BaseModel] | None = SegmentAddToolInput
    credentials: Optional[SegmentCredentials] = None
