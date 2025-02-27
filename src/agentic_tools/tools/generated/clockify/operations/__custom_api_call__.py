from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import ClockifyCredentials

class Clockify__custom_api_call__ToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    task_id: Optional[str] = Field(None, description="ID of task to delete")
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


class Clockify__custom_api_call__Tool(BaseTool):
    name: str = "clockify___custom_api_call__"
    description: str = "Tool for clockify __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Clockify__custom_api_call__ToolInput
    credentials: Optional[ClockifyCredentials] = None
