from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosofttodoCredentials

class MicrosofttodoGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="Task ID")
    task_list_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    display_name: Optional[str] = Field(None, description="Field indicating title of the linked entity")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosofttodoGetallTool(BaseTool):
    name: str = "microsofttodo_getall"
    description: str = "Tool for microsoftToDo getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = MicrosofttodoGetallToolInput
    credentials: Optional[MicrosofttodoCredentials] = None
