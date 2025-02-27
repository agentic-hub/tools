from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import LinearCredentials

class Linear__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    issue_id: Optional[str] = Field(None, description="Issue ID")
    operation: Optional[str] = Field(None, description="Operation")


class Linear__custom_api_call__Tool(BaseTool):
    name: str = "linear___custom_api_call__"
    description: str = "Tool for linear __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Linear__custom_api_call__ToolInput
    credentials: Optional[LinearCredentials] = None
