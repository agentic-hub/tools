from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TodoistCredentials

class TodoistCreateToolInput(BaseModel):
    content: Optional[str] = Field(None, description="Task content")
    resource: Optional[str] = Field(None, description="Resource")
    project: Optional[str] = Field(None, description="ID")
    authentication: Optional[str] = Field(None, description="Authentication")
    options: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistCreateTool(BaseTool):
    name: str = "todoist_create"
    description: str = "Tool for todoist create operation - create operation"
    args_schema: type[BaseModel] | None = TodoistCreateToolInput
    credentials: Optional[TodoistCredentials] = None
