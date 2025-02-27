from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TodoistCredentials

class TodoistReopenToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistReopenTool(BaseTool):
    name: str = "todoist_reopen"
    description: str = "Tool for todoist reopen operation - reopen operation"
    args_schema: type[BaseModel] | None = TodoistReopenToolInput
    credentials: Optional[TodoistCredentials] = None
