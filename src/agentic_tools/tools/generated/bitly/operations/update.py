from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BitlyCredentials

class BitlyUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    deeplink: Optional[Dict[str, Any]] = Field(None, description="Deeplinks")
    id: Optional[str] = Field(None, description="Bitlink")
    operation: Optional[str] = Field(None, description="Operation")


class BitlyUpdateTool(BaseTool):
    name: str = "bitly_update"
    connector_id: str = "nodes-base.bitly"
    description: str = "Tool for bitly update operation - update operation"
    args_schema: type[BaseModel] | None = BitlyUpdateToolInput
    credentials: Optional[BitlyCredentials] = None
