from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BubbleCredentials

class BubbleUpdateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    object_id: Optional[str] = Field(None, description="ID of the object to update")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    type_name: Optional[str] = Field(None, description="Name of data type of the object to update")
    operation: Optional[str] = Field(None, description="Operation")


class BubbleUpdateTool(BaseTool):
    name: str = "bubble_update"
    connector_id: str = "nodes-base.bubble"
    description: str = "Tool for bubble update operation - update operation"
    args_schema: type[BaseModel] | None = BubbleUpdateToolInput
    credentials: Optional[BubbleCredentials] = None
