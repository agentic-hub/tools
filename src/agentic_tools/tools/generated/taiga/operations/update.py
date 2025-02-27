from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TaigaCredentials

class TaigaUpdateToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of the task to update")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    project_id: Optional[str] = Field(None, description="ID of the project to set the epic to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    subject: Optional[str] = Field(None, description="Subject")
    issue_id: Optional[str] = Field(None, description="ID of the issue to update")
    operation: Optional[str] = Field(None, description="Operation")
    user_story_id: Optional[str] = Field(None, description="ID of the user story to update")
    epic_id: Optional[str] = Field(None, description="ID of the epic to update")


class TaigaUpdateTool(BaseTool):
    name: str = "taiga_update"
    connector_id: str = "nodes-base.taiga"
    description: str = "Tool for taiga update operation - update operation"
    args_schema: type[BaseModel] | None = TaigaUpdateToolInput
    credentials: Optional[TaigaCredentials] = None
