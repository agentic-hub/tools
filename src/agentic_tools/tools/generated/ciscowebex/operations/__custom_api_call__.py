from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CiscowebexCredentials

class Ciscowebex__custom_api_call__ToolInput(BaseModel):
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


class Ciscowebex__custom_api_call__Tool(BaseTool):
    name: str = "ciscowebex___custom_api_call__"
    description: str = "Tool for ciscoWebex __CUSTOM_API_CALL__ operation - __CUSTOM_API_CALL__ operation"
    args_schema: type[BaseModel] | None = Ciscowebex__custom_api_call__ToolInput
    credentials: Optional[CiscowebexCredentials] = None
