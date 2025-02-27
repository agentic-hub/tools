from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AutopilotCredentials

class AutopilotRemoveToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="ID of the list to operate on. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    contact_id: Optional[str] = Field(None, description="Can be ID or email")
    operation: Optional[str] = Field(None, description="Operation")


class AutopilotRemoveTool(BaseTool):
    name: str = "autopilot_remove"
    description: str = "Tool for autopilot remove operation - remove operation"
    args_schema: type[BaseModel] | None = AutopilotRemoveToolInput
    credentials: Optional[AutopilotCredentials] = None
