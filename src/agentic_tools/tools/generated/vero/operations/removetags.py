from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VeroCredentials

class VeroRemovetagsToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    tags: Optional[str] = Field(None, description="Tags to remove separated by \",\"")
    data_attributes_json: Optional[str] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    data_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier of the user")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class VeroRemovetagsTool(BaseTool):
    name: str = "vero_removetags"
    connector_id: str = "nodes-base.vero"
    description: str = "Tool for vero removeTags operation - removeTags operation"
    args_schema: type[BaseModel] | None = VeroRemovetagsToolInput
    credentials: Optional[VeroCredentials] = None
