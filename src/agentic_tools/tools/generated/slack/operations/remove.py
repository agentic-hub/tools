from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SlackCredentials

class SlackRemoveToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_ids: Optional[str] = Field(None, description="userIds")
    timestamp: Optional[float] = Field(None, description="Timestamp of the message to add, get or remove")
    file_id: Optional[str] = Field(None, description="File to add star to")
    channel_id: Optional[Dict[str, Any]] = Field(None, description="The Slack channel to get the reactions from")
    text: Optional[str] = Field(None, description="The message text to post. Supports <a href=\"https://api.slack.com/reference/surfaces/formatting\">markdown</a> by default - this can be disabled in \"Options\".")
    select: Optional[str] = Field(None, description="Send Message To")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    user_group_id: Optional[str] = Field(None, description="The encoded ID of the User Group to update")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="Emoji code to use for the message reaction. Use emoji codes like +1, not an actual emoji like 👍. <a target=\"_blank\" href=\" https://www.webfx.com/tools/emoji-cheat-sheet/\">List of common emoji codes</a>")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    ts: Optional[float] = Field(None, description="Timestamp of the message to reply")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    user: Optional[Dict[str, Any]] = Field(None, description="User")


class SlackRemoveTool(BaseTool):
    name: str = "slack_remove"
    description: str = "Tool for slack remove operation - remove operation"
    args_schema: type[BaseModel] | None = SlackRemoveToolInput
    credentials: Optional[SlackCredentials] = None
