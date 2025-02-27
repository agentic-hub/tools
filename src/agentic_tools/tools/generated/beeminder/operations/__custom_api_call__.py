from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import BeeminderCredentials

class Beeminder__custom_api_call__ToolInput(BaseModel):
    goal_name: Optional[str] = Field(None, description="The name of the goal. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    operation: Optional[str] = Field(None, description="Operation")


class Beeminder__custom_api_call__Tool(BaseTool):
    name: str = "beeminder___custom_api_call__"
    connector_id: str = "nodes-base.beeminder"
    description: str = "Tool for beeminder __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Beeminder__custom_api_call__ToolInput
    credentials: Optional[BeeminderCredentials] = None
