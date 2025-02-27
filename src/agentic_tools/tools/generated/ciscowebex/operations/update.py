from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CiscowebexCredentials

class CiscowebexUpdateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    room_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    text: Optional[str] = Field(None, description="The message, in plain text")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    markdown: Optional[bool] = Field(None, description="Whether the message uses markdown")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    message_id: Optional[str] = Field(None, description="ID of the message to update")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    markdown_text: Optional[str] = Field(None, description="The message, in Markdown format. The maximum message length is 7439 bytes.")
    meeting_id: Optional[str] = Field(None, description="ID of the meeting")


class CiscowebexUpdateTool(BaseTool):
    name: str = "ciscowebex_update"
    connector_id: str = "nodes-base.ciscoWebex"
    description: str = "Tool for ciscoWebex update operation - update operation"
    args_schema: type[BaseModel] | None = CiscowebexUpdateToolInput
    credentials: Optional[CiscowebexCredentials] = None
