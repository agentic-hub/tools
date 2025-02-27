from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZendeskCredentials

class ZendeskCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    description: Optional[str] = Field(None, description="The first comment on the ticket")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    additional_fields_json: Optional[str] = Field(None, description="Object of values to set as described <a href=\"https://developer.zendesk.com/rest_api/docs/support/tickets\">here</a>")
    id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The user's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class ZendeskCreateTool(BaseTool):
    name: str = "zendesk_create"
    description: str = "Tool for zendesk create operation - create operation"
    args_schema: type[BaseModel] | None = ZendeskCreateToolInput
    credentials: Optional[ZendeskCredentials] = None
