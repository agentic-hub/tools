from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DriftCredentials

class DriftDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for the contact")
    operation: Optional[str] = Field(None, description="Operation")


class DriftDeleteTool(BaseTool):
    name: str = "drift_delete"
    description: str = "Tool for drift delete operation - delete operation"
    args_schema: type[BaseModel] | None = DriftDeleteToolInput
    credentials: Optional[DriftCredentials] = None
