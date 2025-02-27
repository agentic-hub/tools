from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TodoistCredentials

class TodoistUpdateToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistUpdateTool(BaseTool):
    name: str = "todoist_update"
    connector_id: str = "nodes-base.todoist"
    description: str = "Tool for todoist update operation - update operation"
    args_schema: type[BaseModel] | None = TodoistUpdateToolInput
    credentials: Optional[TodoistCredentials] = None
