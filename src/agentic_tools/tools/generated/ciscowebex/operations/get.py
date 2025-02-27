from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CiscowebexCredentials

class CiscowebexGetToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    text: Optional[str] = Field(None, description="The message, in plain text")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    message_id: Optional[str] = Field(None, description="ID of the message to retrieve")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    meeting_id: Optional[str] = Field(None, description="ID of the meeting")


class CiscowebexGetTool(BaseTool):
    name: str = "ciscowebex_get"
    description: str = "Tool for ciscoWebex get operation - get operation"
    args_schema: type[BaseModel] | None = CiscowebexGetToolInput
    credentials: Optional[CiscowebexCredentials] = None
