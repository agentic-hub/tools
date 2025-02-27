from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZendeskCredentials

class ZendeskGetorganizationsToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    json_parameters: Optional[bool] = Field(None, description="JSON Parameters")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="User ID")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The user's name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")


class ZendeskGetorganizationsTool(BaseTool):
    name: str = "zendesk_getorganizations"
    description: str = "Tool for zendesk getOrganizations operation - getOrganizations operation"
    args_schema: type[BaseModel] | None = ZendeskGetorganizationsToolInput
    credentials: Optional[ZendeskCredentials] = None
