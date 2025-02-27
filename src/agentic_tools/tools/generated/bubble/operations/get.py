from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BubbleCredentials

class BubbleGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    object_id: Optional[str] = Field(None, description="ID of the object to retrieve")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    type_name: Optional[str] = Field(None, description="Name of data type of the object to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class BubbleGetTool(BaseTool):
    name: str = "bubble_get"
    connector_id: str = "nodes-base.bubble"
    description: str = "Tool for bubble get operation - get operation"
    args_schema: type[BaseModel] | None = BubbleGetToolInput
    credentials: Optional[BubbleCredentials] = None
