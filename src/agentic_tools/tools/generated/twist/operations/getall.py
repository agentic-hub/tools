from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import TwistCredentials

class TwistGetallToolInput(BaseModel):
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    content: Optional[str] = Field(None, description="The content of the comment")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Other options to set")
    resource: Optional[str] = Field(None, description="Resource")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    conversation_id: Optional[str] = Field(None, description="The ID of the conversation. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    id: Optional[str] = Field(None, description="The ID of the conversation message")
    workspace_id: Optional[str] = Field(None, description="The ID of the workspace. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    thread_id: Optional[str] = Field(None, description="The ID of the channel")
    comment_id: Optional[str] = Field(None, description="The ID of the comment")
    channel_id: Optional[str] = Field(None, description="The ID of the channel")
    operation: Optional[str] = Field(None, description="Operation")


class TwistGetallTool(BaseTool):
    name: str = "twist_getall"
    description: str = "Tool for twist getAll operation - getAll operation"
    args_schema: type[BaseModel] | None = TwistGetallToolInput
    credentials: Optional[TwistCredentials] = None
