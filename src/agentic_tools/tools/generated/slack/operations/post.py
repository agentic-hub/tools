from agentic_tools.tools import BaseTool, BaseModel, Field
from typing import Optional, Dict, Any, List, Union

from .. import SlackCredentials

class SlackPostToolInput(BaseModel):
    update_fields: Optional[Dict[str, Any]] = Field(None, description="Update Fields")
    user_ids: Optional[str] = Field(None, description="userIds")
    timestamp: Optional[float] = Field(None, description="Timestamp of the message to message")
    file_id: Optional[str] = Field(None, description="File to add star to")
    channel_id: Optional[Dict[str, Any]] = Field(None, description="The Slack channel to send to")
    message_type: Optional[str] = Field(None, description="Whether to send a simple text message, or use Slack’s Blocks UI builder for more sophisticated messages that include form fields, sections and more")
    text: Optional[str] = Field(None, description="The message text to post. Supports <a href=\"https://api.slack.com/reference/surfaces/formatting\">markdown</a> by default - this can be disabled in \"Options\".")
    select: Optional[str] = Field(None, description="Send Message To")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    notice_attachments: Optional[str] = Field(None, description="This is a legacy Slack feature. Slack advises to instead use Blocks.")
    user_group_id: Optional[str] = Field(None, description="The encoded ID of the User Group to update")
    other_options: Optional[Dict[str, Any]] = Field(None, description="Other options to set")
    operation: Optional[str] = Field(None, description="Operation")
    attachments: Optional[List[Any]] = Field(None, description="Attachments")
    name: Optional[str] = Field(None, description="New name for conversation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    filters: Optional[Dict[str, Any]] = Field(None, description="Filters")
    ts: Optional[float] = Field(None, description="Timestamp of the message to reply")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Authentication")
    user: Optional[Dict[str, Any]] = Field(None, description="User")
    blocks_ui: Optional[str] = Field(None, description="Enter the JSON output from Slack's visual Block Kit Builder here. You can then use expressions to add variable content to your blocks. To create blocks, use <a target='_blank' href='https://app.slack.com/block-kit-builder'>Slack's Block Kit Builder</a>")


class SlackPostTool(BaseTool):
    name: str = "slack_post"
    connector_id: str = "nodes-base.slack"
    description: str = "Tool for slack post operation - post operation"
    args_schema: type[BaseModel] | None = SlackPostToolInput
    credentials: Optional[SlackCredentials] = None
