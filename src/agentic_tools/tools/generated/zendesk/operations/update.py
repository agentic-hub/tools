from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZendeskCredentials

class ZendeskUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="Ticket ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The user's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    update_fields_json: Optional[str] = Field(None, description="Object of values to update as described <a href=\"https://developer.zendesk.com/rest_api/docs/support/tickets\">here</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class ZendeskUpdateTool(BaseTool):
    name: str = "zendesk_update"
    description: str = "Tool for zendesk update operation - update operation"
    args_schema: type[BaseModel] | None = ZendeskUpdateToolInput
    credentials: Optional[ZendeskCredentials] = None
