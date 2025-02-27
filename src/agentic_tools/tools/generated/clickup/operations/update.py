from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ClickupCredentials

class ClickupUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    space: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    checklist: Optional[str] = Field(None, description="Checklist ID")
    time_entry_ids: Optional[str] = Field(None, description="Time Entry IDs")
    archived: Optional[bool] = Field(None, description="Archived")
    foreground_color: Optional[str] = Field(None, description="Foreground Color")
    list: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    task: Optional[str] = Field(None, description="Task ID")
    key_result: Optional[str] = Field(None, description="Key Result ID")
    checklist_item: Optional[str] = Field(None, description="Checklist Item ID")
    time_entry: Optional[str] = Field(None, description="Time Entry ID")
    id: Optional[str] = Field(None, description="Task ID")
    operation: Optional[str] = Field(None, description="Operation")
    goal: Optional[str] = Field(None, description="Goal ID")
    task_id: Optional[str] = Field(None, description="Task ID")
    name: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    depends_on_task: Optional[str] = Field(None, description="Depends On Task ID")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    tag_names: Optional[str] = Field(None, description="tagNames")
    folderless: Optional[bool] = Field(None, description="Folderless List")
    comment: Optional[str] = Field(None, description="Comment ID")
    folder: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    background_color: Optional[str] = Field(None, description="Background Color")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    new_name: Optional[str] = Field(None, description="New name to set for the tag")
    authentication: Optional[str] = Field(None, description="Authentication")
    team: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")


class ClickupUpdateTool(BaseTool):
    name: str = "clickup_update"
    description: str = "Tool for clickUp update operation - update operation"
    args_schema: type[BaseModel] | None = ClickupUpdateToolInput
    credentials: Optional[ClickupCredentials] = None
