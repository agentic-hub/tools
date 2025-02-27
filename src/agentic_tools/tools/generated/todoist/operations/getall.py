from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TodoistCredentials

class TodoistGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    authentication: Optional[str] = Field(None, description="Authentication")
    labels: Optional[str] = Field(None, description="labels")
    operation: Optional[str] = Field(None, description="Operation")


class TodoistGetallTool(BaseTool):
    name: str = "todoist_getall"
    description: str = "Tool for todoist getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = TodoistGetallToolInput
    credentials: Optional[TodoistCredentials] = None
