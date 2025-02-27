from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftdynamicscrmCredentials

class MicrosoftdynamicscrmCreateToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Company or business name")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosoftdynamicscrmCreateTool(BaseTool):
    name: str = "microsoftdynamicscrm_create"
    connector_id: str = "nodes-base.microsoftDynamicsCrm"
    description: str = "Tool for microsoftDynamicsCrm create operation - create operation"
    args_schema: type[BaseModel] | None = MicrosoftdynamicscrmCreateToolInput
    credentials: Optional[MicrosoftdynamicscrmCredentials] = None
