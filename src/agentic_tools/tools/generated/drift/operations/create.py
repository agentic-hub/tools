from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DriftCredentials

class DriftCreateToolInput(BaseModel):
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    email: Optional[str] = Field(None, description="The email of the contact")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for the contact")
    operation: Optional[str] = Field(None, description="Operation")


class DriftCreateTool(BaseTool):
    name: str = "drift_create"
    connector_id: str = "nodes-base.drift"
    description: str = "Tool for drift create operation - create operation"
    args_schema: type[BaseModel] | None = DriftCreateToolInput
    credentials: Optional[DriftCredentials] = None
