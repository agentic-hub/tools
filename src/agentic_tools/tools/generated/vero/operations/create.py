from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import VeroCredentials

class VeroCreateToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    tags: Optional[str] = Field(None, description="Tags to add separated by \",\"")
    data_attributes_json: Optional[str] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    data_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="Key value pairs that represent the custom user properties you want to update")
    operation: Optional[str] = Field(None, description="Operation")
    id: Optional[str] = Field(None, description="The unique identifier of the customer")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")


class VeroCreateTool(BaseTool):
    name: str = "vero_create"
    description: str = "Tool for vero create operation - create operation"
    args_schema: type[BaseModel] | None = VeroCreateToolInput
    credentials: Optional[VeroCredentials] = None
