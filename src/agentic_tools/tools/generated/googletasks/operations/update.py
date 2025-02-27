from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogletasksCredentials

class GoogletasksUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="Task ID")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    task: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogletasksUpdateTool(BaseTool):
    name: str = "googletasks_update"
    connector_id: str = "nodes-base.googleTasks"
    description: str = "Tool for googleTasks update operation - update operation"
    args_schema: type[BaseModel] | None = GoogletasksUpdateToolInput
    credentials: Optional[GoogletasksCredentials] = None
