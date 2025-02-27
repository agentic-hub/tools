from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TodoistCredentials

class TodoistDeleteToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistDeleteTool(BaseTool):
    name: str = "todoist_delete"
    connector_id: str = "nodes-base.todoist"
    description: str = "Tool for todoist delete operation - delete operation"
    args_schema: type[BaseModel] | None = TodoistDeleteToolInput
    credentials: Optional[TodoistCredentials] = None
