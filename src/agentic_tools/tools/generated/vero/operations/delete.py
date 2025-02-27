from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VeroCredentials

class VeroDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    tags: Optional[str] = Field(None, description="Tags to add separated by \",\"")
    data_attributes_json: Optional[str] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    data_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier of the user")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class VeroDeleteTool(BaseTool):
    name: str = "vero_delete"
    description: str = "Tool for vero delete operation - delete operation"
    args_schema: type[BaseModel] | None = VeroDeleteToolInput
    credentials: Optional[VeroCredentials] = None
