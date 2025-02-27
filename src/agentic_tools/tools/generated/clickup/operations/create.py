from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ClickupCredentials

class ClickupCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    space: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    checklist: Optional[str] = Field(None, description="Checklist ID")
    time_entry_ids: Optional[str] = Field(None, description="Time Entry IDs")
    foreground_color: Optional[str] = Field(None, description="Foreground Color")
    type: Optional[str] = Field(None, description="Type")
    list: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    task: Optional[str] = Field(None, description="Task ID")
    key_result: Optional[str] = Field(None, description="Key Result ID")
    checklist_item: Optional[str] = Field(None, description="Checklist Item ID")
    comment_text: Optional[str] = Field(None, description="Comment Text")
    time_entry: Optional[str] = Field(None, description="Time Entry ID")
    id: Optional[str] = Field(None, description="ID")
    operation: Optional[str] = Field(None, description="Operation")
    goal: Optional[str] = Field(None, description="Goal ID")
    task_id: Optional[str] = Field(None, description="Task ID")
    name: Optional[str] = Field(None, description="Name")
    start: Optional[str] = Field(None, description="Start")
    depends_on_task: Optional[str] = Field(None, description="Depends On Task ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_names: Optional[str] = Field(None, description="tagNames")
    folderless: Optional[bool] = Field(None, description="Folderless List")
    comment: Optional[str] = Field(None, description="Comment ID")
    comment_on: Optional[str] = Field(None, description="Comment On")
    folder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    background_color: Optional[str] = Field(None, description="Background Color")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    authentication: Optional[str] = Field(None, description="Authentication")
    team: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    duration: Optional[float] = Field(None, description="Duration in minutes")


class ClickupCreateTool(BaseTool):
    name: str = "clickup_create"
    connector_id: str = "nodes-base.clickUp"
    description: str = "Tool for clickUp create operation - create operation"
    args_schema: type[BaseModel] | None = ClickupCreateToolInput
    credentials: Optional[ClickupCredentials] = None
