from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DriftCredentials

class DriftUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for the contact")
    operation: Optional[str] = Field(None, description="Operation")


class DriftUpdateTool(BaseTool):
    name: str = "drift_update"
    description: str = "Tool for drift update operation - update operation"
    args_schema: type[BaseModel] | None = DriftUpdateToolInput
    credentials: Optional[DriftCredentials] = None
