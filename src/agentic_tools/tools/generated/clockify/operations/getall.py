from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ClockifyCredentials

class ClockifyGetallToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of task to delete")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    name: Optional[str] = Field(None, description="Name of client being created")
    client_id: Optional[str] = Field(None, description="Client ID")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    tag_id: Optional[str] = Field(None, description="Tag ID")
    project_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    workspace_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    operation: Optional[str] = Field(None, description="Operation")
    time_entry_id: Optional[str] = Field(None, description="Time Entry ID")


class ClockifyGetallTool(BaseTool):
    name: str = "clockify_getall"
    connector_id: str = "nodes-base.clockify"
    description: str = "Tool for clockify getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = ClockifyGetallToolInput
    credentials: Optional[ClockifyCredentials] = None
