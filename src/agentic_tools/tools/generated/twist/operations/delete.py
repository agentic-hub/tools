from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwistCredentials

class TwistDeleteToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="The content of the comment")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    conversation_id: Optional[str] = Field(None, description="The ID of the conversation. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    id: Optional[str] = Field(None, description="The ID of the conversation message")
    workspace_id: Optional[str] = Field(None, description="The ID of the workspace. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    thread_id: Optional[str] = Field(None, description="The ID of the thread")
    comment_id: Optional[str] = Field(None, description="The ID of the comment")
    channel_id: Optional[str] = Field(None, description="The ID of the channel")
    operation: Optional[str] = Field(None, description="Operation")


class TwistDeleteTool(BaseTool):
    name: str = "twist_delete"
    connector_id: str = "nodes-base.twist"
    description: str = "Tool for twist delete operation - delete operation"
    args_schema: type[BaseModel] | None = TwistDeleteToolInput
    credentials: Optional[TwistCredentials] = None
