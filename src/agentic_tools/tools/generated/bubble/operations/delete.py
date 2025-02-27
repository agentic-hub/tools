from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BubbleCredentials

class BubbleDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    object_id: Optional[str] = Field(None, description="ID of the object to retrieve")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    type_name: Optional[str] = Field(None, description="Name of data type of the object to retrieve")
    operation: Optional[str] = Field(None, description="Operation")


class BubbleDeleteTool(BaseTool):
    name: str = "bubble_delete"
    description: str = "Tool for bubble delete operation - delete operation"
    args_schema: type[BaseModel] | None = BubbleDeleteToolInput
    credentials: Optional[BubbleCredentials] = None
