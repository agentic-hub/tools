from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import GmailCredentials

class GmailMarkasunreadToolInput(BaseModel):
    thread_id: Optional[str] = Field(None, description="The ID of the thread you are operating on")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    subject: Optional[str] = Field(None, description="Subject")
    operation: Optional[str] = Field(None, description="Operation")
    email_type: Optional[str] = Field(None, description="Email Type")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message: Optional[str] = Field(None, description="Message")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    message_id: Optional[str] = Field(None, description="Message ID")
    filters_notice: Optional[str] = Field(None, description="Fetching a lot of messages may take a long time. Consider using filters to speed things up")
    simple: Optional[bool] = Field(None, description="Whether to return a simplified version of the response instead of the raw data")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    label_ids: Optional[str] = Field(None, description="labelIds")


class GmailMarkasunreadTool(BaseTool):
    name: str = "gmail_markasunread"
    description: str = "Tool for gmail markAsUnread operation - markAsUnread operation"
    args_schema: type[BaseModel] | None = GmailMarkasunreadToolInput
    credentials: Optional[GmailCredentials] = None
