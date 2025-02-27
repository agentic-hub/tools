from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import IntercomCredentials

class IntercomCreateToolInput(BaseModel):
    custom_attributes_json: Optional[str] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    value: Optional[str] = Field(None, description="View by value")
    email: Optional[str] = Field(None, description="The email of the user")
    select_by: Optional[str] = Field(None, description="The property to select the user by")
    company_id: Optional[str] = Field(None, description="The company ID you have defined for the company")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    update_by: Optional[str] = Field(None, description="The property via which to query the user")
    identifier_type: Optional[str] = Field(None, description="Unique string identifier")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    id_value: Optional[str] = Field(None, description="Unique string identifier value")
    custom_attributes_ui: Optional[Dict[str, Any]] = Field(None, description="A hash of key/value pairs to represent custom data you want to attribute to a user")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class IntercomCreateTool(BaseTool):
    name: str = "intercom_create"
    connector_id: str = "nodes-base.intercom"
    description: str = "Tool for intercom create operation - create operation"
    args_schema: type[BaseModel] | None = IntercomCreateToolInput
    credentials: Optional[IntercomCredentials] = None
