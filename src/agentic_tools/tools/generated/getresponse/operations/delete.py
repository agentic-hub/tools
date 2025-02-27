from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GetresponseCredentials

class GetresponseDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="ID of contact to delete")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GetresponseDeleteTool(BaseTool):
    name: str = "getresponse_delete"
    connector_id: str = "nodes-base.getResponse"
    description: str = "Tool for getResponse delete operation - delete operation"
    args_schema: type[BaseModel] | None = GetresponseDeleteToolInput
    credentials: Optional[GetresponseCredentials] = None
