from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GetresponseCredentials

class GetresponseGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for a particular contact")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GetresponseGetTool(BaseTool):
    name: str = "getresponse_get"
    description: str = "Tool for getResponse get operation - get operation"
    args_schema: type[BaseModel] | None = GetresponseGetToolInput
    credentials: Optional[GetresponseCredentials] = None
