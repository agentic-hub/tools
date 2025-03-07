from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendgridCredentials

class SendgridUpdateToolInput(BaseModel):
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Primary email for the contact")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="ID of the list")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class SendgridUpdateTool(BaseTool):
    name: str = "sendgrid_update"
    connector_id: str = "nodes-base.sendGrid"
    description: str = "Tool for sendGrid update operation - update operation"
    args_schema: type[BaseModel] | None = SendgridUpdateToolInput
    credentials: Optional[SendgridCredentials] = None
