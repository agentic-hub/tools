from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BeeminderCredentials

class BeeminderDeleteToolInput(BaseModel):
    goal_name: Optional[str] = Field(None, description="The name of the goal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    datapoint_id: Optional[str] = Field(None, description="Datapoint ID")
    operation: Optional[str] = Field(None, description="Operation")


class BeeminderDeleteTool(BaseTool):
    name: str = "beeminder_delete"
    connector_id: str = "nodes-base.beeminder"
    description: str = "Tool for beeminder delete operation - delete operation"
    args_schema: type[BaseModel] | None = BeeminderDeleteToolInput
    credentials: Optional[BeeminderCredentials] = None
