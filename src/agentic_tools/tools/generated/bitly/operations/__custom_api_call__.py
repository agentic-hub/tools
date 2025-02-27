from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BitlyCredentials

class Bitly__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    deeplink: Optional[Dict[str, Any]] = Field(None, description="Deeplinks")
    id: Optional[str] = Field(None, description="Bitlink")
    operation: Optional[str] = Field(None, description="Operation")


class Bitly__custom_api_call__Tool(BaseTool):
    name: str = "bitly___custom_api_call__"
    connector_id: str = "nodes-base.bitly"
    description: str = "Tool for bitly __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Bitly__custom_api_call__ToolInput
    credentials: Optional[BitlyCredentials] = None
