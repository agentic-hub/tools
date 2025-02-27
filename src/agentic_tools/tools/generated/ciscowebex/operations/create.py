from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import CiscowebexCredentials

class CiscowebexCreateToolInput(BaseModel):
    room_id: Optional[str] = Field(None, description="Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>")
    to_person_id: Optional[str] = Field(None, description="Person ID")
    text: Optional[str] = Field(None, description="The message, in plain text")
    specify_person_by: Optional[str] = Field(None, description="Specify Person By")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    end: Optional[str] = Field(None, description="Date and time for the end of the meeting. Acceptable <a href=\"https://datatracker.ietf.org/doc/html/rfc2445\"> format</a>.")
    to_person_email: Optional[str] = Field(None, description="Person Email")
    operation: Optional[str] = Field(None, description="Operation")
    start: Optional[str] = Field(None, description="Date and time for the start of the meeting. Acceptable <a href=\"https://datatracker.ietf.org/doc/html/rfc2445\"> format</a>.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    destination: Optional[str] = Field(None, description="Destination")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    message_id: Optional[str] = Field(None, description="ID of the message to delete")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    meeting_id: Optional[str] = Field(None, description="ID of the meeting")
    title: Optional[str] = Field(None, description="Meeting title. The title can be a maximum of 128 characters long.")


class CiscowebexCreateTool(BaseTool):
    name: str = "ciscowebex_create"
    description: str = "Tool for ciscoWebex create operation - create operation"
    args_schema: type[BaseModel] | None = CiscowebexCreateToolInput
    credentials: Optional[CiscowebexCredentials] = None
