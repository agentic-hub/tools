from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import PushoverCredentials

class Pushover__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Pushover__custom_api_call__Tool(BaseTool):
    name: str = "pushover___custom_api_call__"
    description: str = "Tool for pushover __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Pushover__custom_api_call__ToolInput
    credentials: Optional[PushoverCredentials] = None
