from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AwssnsCredentials

class Awssns__custom_api_call__ToolInput(BaseModel):
    operation: Optional[str] = Field(None, description="Operation")


class Awssns__custom_api_call__Tool(BaseTool):
    name: str = "awssns___custom_api_call__"
    description: str = "Tool for awsSns __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Awssns__custom_api_call__ToolInput
    credentials: Optional[AwssnsCredentials] = None
