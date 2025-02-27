from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DhlCredentials

class DhlGetToolInput(BaseModel):
    tracking_number: Optional[str] = Field(None, description="Tracking Number")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class DhlGetTool(BaseTool):
    name: str = "dhl_get"
    description: str = "Tool for dhl get operation - get operation"
    args_schema: type[BaseModel] | None = DhlGetToolInput
    credentials: Optional[DhlCredentials] = None
