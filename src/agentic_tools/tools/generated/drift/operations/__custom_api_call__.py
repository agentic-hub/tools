from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DriftCredentials

class Drift__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for the contact")
    operation: Optional[str] = Field(None, description="Operation")


class Drift__custom_api_call__Tool(BaseTool):
    name: str = "drift___custom_api_call__"
    connector_id: str = "nodes-base.drift"
    description: str = "Tool for drift __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Drift__custom_api_call__ToolInput
    credentials: Optional[DriftCredentials] = None
