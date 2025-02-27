from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AutomizyCredentials

class AutomizyDeleteToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    list_id: Optional[str] = Field(None, description="List ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of the contact")
    contact_id: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutomizyDeleteTool(BaseTool):
    name: str = "automizy_delete"
    connector_id: str = "nodes-base.automizy"
    description: str = "Tool for automizy delete operation - delete operation"
    args_schema: type[BaseModel] | None = AutomizyDeleteToolInput
    credentials: Optional[AutomizyCredentials] = None
