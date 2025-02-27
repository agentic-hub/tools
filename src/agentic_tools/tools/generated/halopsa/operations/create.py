from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import HalopsaCredentials

class HalopsaCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    site_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    summary: Optional[str] = Field(None, description="Summary")
    select_option: Optional[bool] = Field(None, description="Whether client can be selected by ID")
    ticket_type: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    details: Optional[str] = Field(None, description="Details")
    user_id: Optional[str] = Field(None, description="User ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    ticket_id: Optional[str] = Field(None, description="Ticket ID")
    client_name: Optional[str] = Field(None, description="Enter client name")
    operation: Optional[str] = Field(None, description="Operation")
    client_id: Optional[str] = Field(None, description="Client ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    simplify: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    user_name: Optional[str] = Field(None, description="Enter user name")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    site_name: Optional[str] = Field(None, description="Enter site name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")


class HalopsaCreateTool(BaseTool):
    name: str = "halopsa_create"
    connector_id: str = "nodes-base.haloPSA"
    description: str = "Tool for haloPSA create operation - create operation"
    args_schema: type[BaseModel] | None = HalopsaCreateToolInput
    credentials: Optional[HalopsaCredentials] = None
