from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftdynamicscrmCredentials

class MicrosoftdynamicscrmUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")
    account_id: Optional[str] = Field(None, description="Account ID")


class MicrosoftdynamicscrmUpdateTool(BaseTool):
    name: str = "microsoftdynamicscrm_update"
    description: str = "Tool for microsoftDynamicsCrm update operation - update operation"
    args_schema: type[BaseModel] | None = MicrosoftdynamicscrmUpdateToolInput
    credentials: Optional[MicrosoftdynamicscrmCredentials] = None
