from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import MicrosoftoutlookCredentials

class MicrosoftoutlookDeleteToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    output: Optional[str] = Field(None, description="Output")
    display_name: Optional[str] = Field(None, description="Name of the folder")
    attachment_id: Optional[Dict[str, Any]] = Field(None, description="Attachment")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    binary_property_name: Optional[str] = Field(None, description="Input Data Field Name")
    subject: Optional[str] = Field(None, description="The subject of the message")
    folder_id: Optional[Dict[str, Any]] = Field(None, description="Folder")
    draft_id: Optional[Dict[str, Any]] = Field(None, description="Draft")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    filters_ui: Optional[Dict[str, Any]] = Field(None, description="Filters")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    calendar_id: Optional[Dict[str, Any]] = Field(None, description="Calendar")
    body_content: Optional[str] = Field(None, description="Message body content")
    fields: Optional[str] = Field(None, description="fields")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    message_id: Optional[Dict[str, Any]] = Field(None, description="Message")
    event_id: Optional[Dict[str, Any]] = Field(None, description="Event")
    filters_notice: Optional[str] = Field(None, description="Fetching a lot of messages may take a long time. Consider using filters to speed things up")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")
    resource: Optional[str] = Field(None, description="Resource")
    contact_id: Optional[Dict[str, Any]] = Field(None, description="Contact")


class MicrosoftoutlookDeleteTool(BaseTool):
    name: str = "microsoftoutlook_delete"
    description: str = "Tool for microsoftOutlook delete operation - delete operation"
    args_schema: type[BaseModel] | None = MicrosoftoutlookDeleteToolInput
    credentials: Optional[MicrosoftoutlookCredentials] = None
