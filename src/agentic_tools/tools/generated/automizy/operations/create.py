from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AutomizyCredentials

class AutomizyCreateToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    list_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    email: Optional[str] = Field(None, description="The email address of the contact")
    contact_id: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutomizyCreateTool(BaseTool):
    name: str = "automizy_create"
    connector_id: str = "nodes-base.automizy"
    description: str = "Tool for automizy create operation - create operation"
    args_schema: type[BaseModel] | None = AutomizyCreateToolInput
    credentials: Optional[AutomizyCredentials] = None
