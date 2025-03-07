from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TodoistCredentials

class TodoistCloseToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistCloseTool(BaseTool):
    name: str = "todoist_close"
    connector_id: str = "nodes-base.todoist"
    description: str = "Tool for todoist close operation - close operation"
    args_schema: type[BaseModel] | None = TodoistCloseToolInput
    credentials: Optional[TodoistCredentials] = None
