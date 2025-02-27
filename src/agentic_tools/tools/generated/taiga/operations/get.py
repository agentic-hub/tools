from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TaigaCredentials

class TaigaGetToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of the task to retrieve")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project_id: Optional[str] = Field(None, description="ID of the project to which the epic belongs. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subject: Optional[str] = Field(None, description="Subject")
    issue_id: Optional[str] = Field(None, description="ID of the issue to retrieve")
    operation: Optional[str] = Field(None, description="Operation")
    user_story_id: Optional[str] = Field(None, description="ID of the user story to retrieve")
    epic_id: Optional[str] = Field(None, description="ID of the epic to retrieve")


class TaigaGetTool(BaseTool):
    name: str = "taiga_get"
    connector_id: str = "nodes-base.taiga"
    description: str = "Tool for taiga get operation - get operation"
    args_schema: type[BaseModel] | None = TaigaGetToolInput
    credentials: Optional[TaigaCredentials] = None
