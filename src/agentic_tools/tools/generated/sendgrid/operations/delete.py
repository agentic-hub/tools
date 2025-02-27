from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SendgridCredentials

class SendgridDeleteToolInput(BaseModel):
    ids: Optional[str] = Field(None, description="ID of the contact. Multiple can be added separated by comma.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    delete_contacts: Optional[bool] = Field(None, description="Whether to delete all contacts on the list")
    email: Optional[str] = Field(None, description="Primary email for the contact")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Name of the list")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="ID of the list")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    delete_all: Optional[bool] = Field(None, description="Whether all contacts will be deleted")


class SendgridDeleteTool(BaseTool):
    name: str = "sendgrid_delete"
    description: str = "Tool for sendGrid delete operation - delete operation"
    args_schema: type[BaseModel] | None = SendgridDeleteToolInput
    credentials: Optional[SendgridCredentials] = None
