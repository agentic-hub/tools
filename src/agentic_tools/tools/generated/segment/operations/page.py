from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SegmentCredentials

class SegmentPageToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name of the page For example, most sites have a “Signup” page that can be useful to tag, so you can see users as they move through your funnel")
    user_id: Optional[str] = Field(None, description="User ID")
    resource: Optional[str] = Field(None, description="Resource")
    context: Optional[Dict[str, Any]] = Field(None, description="Context")
    integrations: Optional[Dict[str, Any]] = Field(None, description="Integration")
    traits: Optional[Dict[str, Any]] = Field(None, description="Traits")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class SegmentPageTool(BaseTool):
    name: str = "segment_page"
    connector_id: str = "nodes-base.segment"
    description: str = "Tool for segment page operation - page operation"
    args_schema: type[BaseModel] | None = SegmentPageToolInput
    credentials: Optional[SegmentCredentials] = None
