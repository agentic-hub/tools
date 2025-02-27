from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BeeminderCredentials

class BeeminderGetallToolInput(BaseModel):
    goal_name: Optional[str] = Field(None, description="The name of the goal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    operation: Optional[str] = Field(None, description="Operation")


class BeeminderGetallTool(BaseTool):
    name: str = "beeminder_getall"
    connector_id: str = "nodes-base.beeminder"
    description: str = "Tool for beeminder getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = BeeminderGetallToolInput
    credentials: Optional[BeeminderCredentials] = None
