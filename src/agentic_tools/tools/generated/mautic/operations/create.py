from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MauticCredentials

class MauticCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    position: Optional[str] = Field(None, description="Position")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    company: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    body_json: Optional[str] = Field(None, description="Contact parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    last_name: Optional[str] = Field(None, description="Last Name")
    email: Optional[str] = Field(None, description="Email address of the contact")
    company_id: Optional[str] = Field(None, description="The ID of the company to update")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the company to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    first_name: Optional[str] = Field(None, description="First Name")
    action: Optional[str] = Field(None, description="Action")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    title: Optional[str] = Field(None, description="Title")


class MauticCreateTool(BaseTool):
    name: str = "mautic_create"
    description: str = "Tool for mautic create operation - create operation"
    args_schema: type[BaseModel] | None = MauticCreateToolInput
    credentials: Optional[MauticCredentials] = None
