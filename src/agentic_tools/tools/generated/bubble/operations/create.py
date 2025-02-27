from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BubbleCredentials

class BubbleCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    object_id: Optional[str] = Field(None, description="ID of the object to retrieve")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    type_name: Optional[str] = Field(None, description="Name of data type of the object to create")
    operation: Optional[str] = Field(None, description="Operation")


class BubbleCreateTool(BaseTool):
    name: str = "bubble_create"
    description: str = "Tool for bubble create operation - create operation"
    args_schema: type[BaseModel] | None = BubbleCreateToolInput
    credentials: Optional[BubbleCredentials] = None
