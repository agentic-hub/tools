from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosofttodoCredentials

class MicrosofttodoCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="Task ID")
    task_list_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    title: Optional[str] = Field(None, description="A brief description of the task")
    display_name: Optional[str] = Field(None, description="Field indicating title of the linked entity")
    application_name: Optional[str] = Field(None, description="App name of the source that is sending the linked entity")
    operation: Optional[str] = Field(None, description="Operation")


class MicrosofttodoCreateTool(BaseTool):
    name: str = "microsofttodo_create"
    connector_id: str = "nodes-base.microsoftToDo"
    description: str = "Tool for microsoftToDo create operation - create operation"
    args_schema: type[BaseModel] | None = MicrosofttodoCreateToolInput
    credentials: Optional[MicrosofttodoCredentials] = None
