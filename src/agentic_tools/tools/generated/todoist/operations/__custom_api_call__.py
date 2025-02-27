from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TodoistCredentials

class Todoist__custom_api_call__ToolInput(BaseModel):
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class Todoist__custom_api_call__Tool(BaseTool):
    name: str = "todoist___custom_api_call__"
    connector_id: str = "nodes-base.todoist"
    description: str = "Tool for todoist __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Todoist__custom_api_call__ToolInput
    credentials: Optional[TodoistCredentials] = None
