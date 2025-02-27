from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendgridCredentials

class SendgridGetToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email of the contact")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="ID of the list")
    by: Optional[str] = Field(None, description="Search the user by ID or email")
    contact_sample: Optional[bool] = Field(None, description="Whether to return the contact sample")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    contact_id: Optional[str] = Field(None, description="ID of the contact")


class SendgridGetTool(BaseTool):
    name: str = "sendgrid_get"
    connector_id: str = "nodes-base.sendGrid"
    description: str = "Tool for sendGrid get operation - get operation"
    args_schema: type[BaseModel] | None = SendgridGetToolInput
    credentials: Optional[SendgridCredentials] = None
