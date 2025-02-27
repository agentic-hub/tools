from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CiscowebexCredentials

class CiscowebexDeleteToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    text: Optional[str] = Field(None, description="The message, in plain text")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    message_id: Optional[str] = Field(None, description="ID of the message to delete")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    meeting_id: Optional[str] = Field(None, description="ID of the meeting")


class CiscowebexDeleteTool(BaseTool):
    name: str = "ciscowebex_delete"
    description: str = "Tool for ciscoWebex delete operation - delete operation"
    args_schema: type[BaseModel] | None = CiscowebexDeleteToolInput
    credentials: Optional[CiscowebexCredentials] = None
