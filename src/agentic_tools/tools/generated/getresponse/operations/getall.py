from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GetresponseCredentials

class GetresponseGetallToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="ID of contact to delete")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GetresponseGetallTool(BaseTool):
    name: str = "getresponse_getall"
    connector_id: str = "nodes-base.getResponse"
    description: str = "Tool for getResponse getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GetresponseGetallToolInput
    credentials: Optional[GetresponseCredentials] = None
