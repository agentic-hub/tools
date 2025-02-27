from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BitlyCredentials

class BitlyGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    deeplink: Optional[Dict[str, Any]] = Field(None, description="Deeplinks")
    id: Optional[str] = Field(None, description="Bitlink")
    operation: Optional[str] = Field(None, description="Operation")


class BitlyGetTool(BaseTool):
    name: str = "bitly_get"
    connector_id: str = "nodes-base.bitly"
    description: str = "Tool for bitly get operation - get operation"
    args_schema: type[BaseModel] | None = BitlyGetToolInput
    credentials: Optional[BitlyCredentials] = None
