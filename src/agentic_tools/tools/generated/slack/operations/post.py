from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SlackCredentials(BaseModel):
    """Credentials for slack authentication."""
    slack_api: Optional[Dict[str, Any]] = Field(None, description="slackApi")
    slack_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="slackOAuth2Api")

class SlackPostToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SlackCredentials] = Field(None, description="Custom credentials for authentication")
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
    name = "slack_post"
    description = "Tool for slack post operation - post operation"
    
    def __init__(self, credentials: Optional[SlackCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the slack post operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running slack post operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running slack post operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the slack post operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
