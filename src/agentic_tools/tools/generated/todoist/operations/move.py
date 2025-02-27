from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TodoistCredentials

class TodoistMoveToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    resource: Optional[str] = Field(None, description="Resource")
    project: Optional[str] = Field(None, description="ID")
    authentication: Optional[str] = Field(None, description="Authentication")
    section: Optional[str] = Field(None, description="Section to which you want move the task. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistMoveTool(BaseTool):
    name: str = "todoist_move"
    description: str = "Tool for todoist move operation - move operation"
    args_schema: type[BaseModel] | None = TodoistMoveToolInput
    credentials: Optional[TodoistCredentials] = None
