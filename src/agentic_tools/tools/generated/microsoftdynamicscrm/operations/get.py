from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftdynamicscrmCredentials

class MicrosoftdynamicscrmGetToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Account ID")


class MicrosoftdynamicscrmGetTool(BaseTool):
    name: str = "microsoftdynamicscrm_get"
    connector_id: str = "nodes-base.microsoftDynamicsCrm"
    description: str = "Tool for microsoftDynamicsCrm get operation - get operation"
    args_schema: type[BaseModel] | None = MicrosoftdynamicscrmGetToolInput
    credentials: Optional[MicrosoftdynamicscrmCredentials] = None
