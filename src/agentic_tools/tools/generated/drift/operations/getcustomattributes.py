from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import DriftCredentials

class DriftGetcustomattributesToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    contact_id: Optional[str] = Field(None, description="Unique identifier for the contact")
    operation: Optional[str] = Field(None, description="Operation")


class DriftGetcustomattributesTool(BaseTool):
    name: str = "drift_getcustomattributes"
    connector_id: str = "nodes-base.drift"
    description: str = "Tool for drift getCustomAttributes operation - getCustomAttributes operation"
    args_schema: type[BaseModel] | None = DriftGetcustomattributesToolInput
    credentials: Optional[DriftCredentials] = None
