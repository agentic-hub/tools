from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import AsanaCredentials

class AsanaGetallToolInput(BaseModel):
    workspace: Optional[str] = Field(None, description="The workspace in which to get users. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    tag: Optional[str] = Field(None, description="The tag that should be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    text: Optional[str] = Field(None, description="The plain text of the comment to add")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    id: Optional[str] = Field(None, description="The ID of the task to delete")
    operation: Optional[str] = Field(None, description="Operation")
    task_id: Optional[str] = Field(None, description="The task to operate on")
    name: Optional[str] = Field(None, description="The name of the subtask to create")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project: Optional[str] = Field(None, description="The project where the task will be added. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Properties to search for")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Other properties to set")
    authentication: Optional[str] = Field(None, description="Authentication")
    other_properties: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class AsanaGetallTool(BaseTool):
    name: str = "asana_getall"
    description: str = "Tool for asana getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = AsanaGetallToolInput
    credentials: Optional[AsanaCredentials] = None
