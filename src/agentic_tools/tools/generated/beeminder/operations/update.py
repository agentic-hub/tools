from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BeeminderCredentials

class BeeminderUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    goal_name: Optional[str] = Field(None, description="The name of the goal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    datapoint_id: Optional[str] = Field(None, description="Datapoint ID")
    operation: Optional[str] = Field(None, description="Operation")


class BeeminderUpdateTool(BaseTool):
    name: str = "beeminder_update"
    connector_id: str = "nodes-base.beeminder"
    description: str = "Tool for beeminder update operation - update operation"
    args_schema: type[BaseModel] | None = BeeminderUpdateToolInput
    credentials: Optional[BeeminderCredentials] = None
