from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import IntercomCredentials

class IntercomGetToolInput(BaseModel):
    custom_attributes_json: Optional[str] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="View by value")
    select_by: Optional[str] = Field(None, description="The property to select the user by")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    update_by: Optional[str] = Field(None, description="The property via which to query the user")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    custom_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class IntercomGetTool(BaseTool):
    name: str = "intercom_get"
    description: str = "Tool for intercom get operation - get operation"
    args_schema: type[BaseModel] | None = IntercomGetToolInput
    credentials: Optional[IntercomCredentials] = None
