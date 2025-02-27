from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BeeminderCredentials

class BeeminderCreateToolInput(BaseModel):
    goal_name: Optional[str] = Field(None, description="The name of the goal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    value: Optional[float] = Field(None, description="Datapoint value to send")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    operation: Optional[str] = Field(None, description="Operation")


class BeeminderCreateTool(BaseTool):
    name: str = "beeminder_create"
    connector_id: str = "nodes-base.beeminder"
    description: str = "Tool for beeminder create operation - create operation"
    args_schema: type[BaseModel] | None = BeeminderCreateToolInput
    credentials: Optional[BeeminderCredentials] = None
