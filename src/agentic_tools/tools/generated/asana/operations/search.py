from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AsanaCredentials

class AsanaSearchToolInput(BaseModel):
    workspace: Optional[str] = Field(None, description="The workspace in which the task is searched. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    tag: Optional[str] = Field(None, description="The tag that should be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    text: Optional[str] = Field(None, description="The plain text of the comment to add")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    search_task_properties: Optional[Dict[str, Any]] = Field(None, description="Properties to search for")
    id: Optional[str] = Field(None, description="The ID of the task to delete")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="The task to operate on")
    name: Optional[str] = Field(None, description="The name of the subtask to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project: Optional[str] = Field(None, description="The project where the task will be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Properties of the task comment")
    authentication: Optional[str] = Field(None, description="Authentication")
    other_properties: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class AsanaSearchTool(BaseTool):
    name: str = "asana_search"
    description: str = "Tool for asana search operation - search operation"
    args_schema: type[BaseModel] | None = AsanaSearchToolInput
    credentials: Optional[AsanaCredentials] = None
