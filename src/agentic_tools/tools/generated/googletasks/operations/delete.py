from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogletasksCredentials

class GoogletasksDeleteToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    task: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogletasksDeleteTool(BaseTool):
    name: str = "googletasks_delete"
    connector_id: str = "nodes-base.googleTasks"
    description: str = "Tool for googleTasks delete operation - delete operation"
    args_schema: type[BaseModel] | None = GoogletasksDeleteToolInput
    credentials: Optional[GoogletasksCredentials] = None
