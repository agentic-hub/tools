from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TodoistCredentials

class TodoistGetToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistGetTool(BaseTool):
    name: str = "todoist_get"
    description: str = "Tool for todoist get operation - get operation"
    args_schema: type[BaseModel] | None = TodoistGetToolInput
    credentials: Optional[TodoistCredentials] = None
