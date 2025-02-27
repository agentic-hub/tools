from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DriftCredentials

class DriftGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for the contact")
    operation: Optional[str] = Field(None, description="Operation")


class DriftGetTool(BaseTool):
    name: str = "drift_get"
    description: str = "Tool for drift get operation - get operation"
    args_schema: type[BaseModel] | None = DriftGetToolInput
    credentials: Optional[DriftCredentials] = None
