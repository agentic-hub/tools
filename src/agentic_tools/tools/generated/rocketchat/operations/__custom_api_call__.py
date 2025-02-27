from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import RocketchatCredentials

class Rocketchat__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Rocketchat__custom_api_call__Tool(BaseTool):
    name: str = "rocketchat___custom_api_call__"
    connector_id: str = "nodes-base.rocketchat"
    description: str = "Tool for rocketchat __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Rocketchat__custom_api_call__ToolInput
    credentials: Optional[RocketchatCredentials] = None
