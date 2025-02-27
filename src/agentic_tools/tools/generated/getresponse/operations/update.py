from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GetresponseCredentials

class GetresponseUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for a particular contact")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class GetresponseUpdateTool(BaseTool):
    name: str = "getresponse_update"
    description: str = "Tool for getResponse update operation - update operation"
    args_schema: type[BaseModel] | None = GetresponseUpdateToolInput
    credentials: Optional[GetresponseCredentials] = None
