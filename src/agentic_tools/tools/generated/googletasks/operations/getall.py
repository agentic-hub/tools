from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GoogletasksCredentials

class GoogletasksGetallToolInput(BaseModel):
    task_id: Optional[str] = Field(None, description="Task ID")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    task: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")


class GoogletasksGetallTool(BaseTool):
    name: str = "googletasks_getall"
    description: str = "Tool for googleTasks getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = GoogletasksGetallToolInput
    credentials: Optional[GoogletasksCredentials] = None
