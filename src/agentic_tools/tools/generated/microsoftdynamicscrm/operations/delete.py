from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftdynamicscrmCredentials

class MicrosoftdynamicscrmDeleteToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Account ID")


class MicrosoftdynamicscrmDeleteTool(BaseTool):
    name: str = "microsoftdynamicscrm_delete"
    description: str = "Tool for microsoftDynamicsCrm delete operation - delete operation"
    args_schema: type[BaseModel] | None = MicrosoftdynamicscrmDeleteToolInput
    credentials: Optional[MicrosoftdynamicscrmCredentials] = None
