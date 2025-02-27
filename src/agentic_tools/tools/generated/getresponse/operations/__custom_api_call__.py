from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GetresponseCredentials

class Getresponse__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="ID of contact to delete")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class Getresponse__custom_api_call__Tool(BaseTool):
    name: str = "getresponse___custom_api_call__"
    description: str = "Tool for getResponse __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Getresponse__custom_api_call__ToolInput
    credentials: Optional[GetresponseCredentials] = None
