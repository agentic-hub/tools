from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SegmentCredentials

class Segment__custom_api_call__ToolInput(BaseModel):
    user_id: Optional[str] = Field(None, description="User ID")
    resource: Optional[str] = Field(None, description="Resource")
    context: Optional[Dict[str, Any]] = Field(None, description="Context")
    integrations: Optional[Dict[str, Any]] = Field(None, description="Integration")
    traits: Optional[Dict[str, Any]] = Field(None, description="Traits")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    operation: Optional[str] = Field(None, description="Operation")


class Segment__custom_api_call__Tool(BaseTool):
    name: str = "segment___custom_api_call__"
    description: str = "Tool for segment __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Segment__custom_api_call__ToolInput
    credentials: Optional[SegmentCredentials] = None
