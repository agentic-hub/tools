from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AutopilotCredentials

class AutopilotCreateToolInput(BaseModel):
    name: Optional[str] = Field(None, description="Name of the list to create")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    contact_id: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutopilotCreateTool(BaseTool):
    name: str = "autopilot_create"
    description: str = "Tool for autopilot create operation - create operation"
    args_schema: type[BaseModel] | None = AutopilotCreateToolInput
    credentials: Optional[AutopilotCredentials] = None
