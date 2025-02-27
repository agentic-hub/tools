from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwakeCredentials

class Twake__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Twake__custom_api_call__Tool(BaseTool):
    name: str = "twake___custom_api_call__"
    connector_id: str = "nodes-base.twake"
    description: str = "Tool for twake __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Twake__custom_api_call__ToolInput
    credentials: Optional[TwakeCredentials] = None
