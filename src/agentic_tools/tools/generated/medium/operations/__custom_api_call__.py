from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MediumCredentials

class Medium__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    operation: Optional[str] = Field(None, description="Operation")


class Medium__custom_api_call__Tool(BaseTool):
    name: str = "medium___custom_api_call__"
    description: str = "Tool for medium __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Medium__custom_api_call__ToolInput
    credentials: Optional[MediumCredentials] = None
