from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GetresponseCredentials

class GetresponseCreateToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    campaign_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    email: Optional[str] = Field(None, description="Email")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="ID of contact to delete")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GetresponseCreateTool(BaseTool):
    name: str = "getresponse_create"
    description: str = "Tool for getResponse create operation - create operation"
    args_schema: type[BaseModel] | None = GetresponseCreateToolInput
    credentials: Optional[GetresponseCredentials] = None
