from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BitlyCredentials

class BitlyCreateToolInput(BaseModel):
    long_url: Optional[str] = Field(None, description="Long URL")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    deeplink: Optional[Dict[str, Any]] = Field(None, description="Deeplinks")
    id: Optional[str] = Field(None, description="Bitlink")
    operation: Optional[str] = Field(None, description="Operation")


class BitlyCreateTool(BaseTool):
    name: str = "bitly_create"
    connector_id: str = "nodes-base.bitly"
    description: str = "Tool for bitly create operation - create operation"
    args_schema: type[BaseModel] | None = BitlyCreateToolInput
    credentials: Optional[BitlyCredentials] = None
