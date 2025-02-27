from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SlackCredentials

class SlackCreateToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_ids: Optional[str] = Field(None, description="userIds")
    timestamp: Optional[float] = Field(None, description="Timestamp of the message to message")
    file_id: Optional[str] = Field(None, description="File to add star to")
    channel_id: Optional[str] = Field(None, description="Channel")
    text: Optional[str] = Field(None, description="The message text to post. Supports <a href=\"https://api.slack.com/reference/surfaces/formatting\">markdown</a> by default - this can be disabled in \"Options\".")
    select: Optional[str] = Field(None, description="Send Message To")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    user_group_id: Optional[str] = Field(None, description="The encoded ID of the User Group to update")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="A name for the User Group. Must be unique among User Groups.")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    channel_visibility: Optional[str] = Field(None, description="Whether to create a Public or a Private Slack channel. <a href=\"https://slack.com/help/articles/360017938993-What-is-a-channel\">More info</a>.")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    ts: Optional[float] = Field(None, description="Timestamp of the message to reply")
    resource: Optional[str] = Field(None, description="Resource")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    authentication: Optional[str] = Field(None, description="Authentication")
    user: Optional[Dict[str, Any]] = Field(None, description="User")


class SlackCreateTool(BaseTool):
    name: str = "slack_create"
    description: str = "Tool for slack create operation - create operation"
    args_schema: type[BaseModel] | None = SlackCreateToolInput
    credentials: Optional[SlackCredentials] = None
