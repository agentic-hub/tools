from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BubbleCredentials

class BubbleGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    object_id: Optional[str] = Field(None, description="ID of the object to retrieve")
    properties: Optional[Dict[str, Any]] = Field(None, description="Properties")
    type_name: Optional[str] = Field(None, description="Name of data type of the object to create")
    operation: Optional[str] = Field(None, description="Operation")


class BubbleGetallTool(BaseTool):
    name: str = "bubble_getall"
    connector_id: str = "nodes-base.bubble"
    description: str = "Tool for bubble getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = BubbleGetallToolInput
    credentials: Optional[BubbleCredentials] = None
