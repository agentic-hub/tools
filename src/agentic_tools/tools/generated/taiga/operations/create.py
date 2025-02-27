from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TaigaCredentials

class TaigaCreateToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of the task to delete")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project_id: Optional[str] = Field(None, description="ID of the project to which the epic belongs. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subject: Optional[str] = Field(None, description="Subject")
    issue_id: Optional[str] = Field(None, description="ID of the issue to delete")
    operation: Optional[str] = Field(None, description="Operation")
    user_story_id: Optional[str] = Field(None, description="ID of the user story to delete")
    epic_id: Optional[str] = Field(None, description="ID of the epic to delete")


class TaigaCreateTool(BaseTool):
    name: str = "taiga_create"
    description: str = "Tool for taiga create operation - create operation"
    args_schema: type[BaseModel] | None = TaigaCreateToolInput
    credentials: Optional[TaigaCredentials] = None
