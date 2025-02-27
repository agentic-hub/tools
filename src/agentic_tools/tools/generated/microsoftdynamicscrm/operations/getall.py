from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftdynamicscrmCredentials

class MicrosoftdynamicscrmGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosoftdynamicscrmGetallTool(BaseTool):
    name: str = "microsoftdynamicscrm_getall"
    connector_id: str = "nodes-base.microsoftDynamicsCrm"
    description: str = "Tool for microsoftDynamicsCrm getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = MicrosoftdynamicscrmGetallToolInput
    credentials: Optional[MicrosoftdynamicscrmCredentials] = None
