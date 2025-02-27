from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ZammadCredentials

class ZammadCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    article: Optional[Dict[str, Any]] = Field(None, description="Article")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="Group to update. Specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    operation: Optional[str] = Field(None, description="Operation")
    customer: Optional[str] = Field(None, description="Email address of the customer concerned in the ticket to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    lastname: Optional[str] = Field(None, description="Last Name")
    name: Optional[str] = Field(None, description="Group Name")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    group: Optional[str] = Field(None, description="Group that will own the ticket to create. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    firstname: Optional[str] = Field(None, description="First Name")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    title: Optional[str] = Field(None, description="Title of the ticket to create")


class ZammadCreateTool(BaseTool):
    name: str = "zammad_create"
    description: str = "Tool for zammad create operation - create operation"
    args_schema: type[BaseModel] | None = ZammadCreateToolInput
    credentials: Optional[ZammadCredentials] = None
