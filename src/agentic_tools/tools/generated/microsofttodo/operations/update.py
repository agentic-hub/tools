from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosofttodoCredentials

class MicrosofttodoUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="Task ID")
    task_list_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    list_id: Optional[str] = Field(None, description="The identifier of the list, unique in the user's mailbox")
    linked_resource_id: Optional[str] = Field(None, description="Linked Resource ID")
    display_name: Optional[str] = Field(None, description="List display name")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosofttodoUpdateTool(BaseTool):
    name: str = "microsofttodo_update"
    description: str = "Tool for microsoftToDo update operation - update operation"
    args_schema: type[BaseModel] | None = MicrosofttodoUpdateToolInput
    credentials: Optional[MicrosofttodoCredentials] = None
