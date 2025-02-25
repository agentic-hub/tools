from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class SlackCredentials(BaseModel):
    """Credentials for slack authentication."""
    slack_api: Optional[Dict[str, Any]] = Field(None, description="slackApi")
    slack_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="slackOAuth2Api")

class SlackRemoveToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[SlackCredentials] = Field(None, description="Custom credentials for authentication")
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
    name = "slack_remove"
    description = "Tool for slack remove operation - remove operation"
    
    def __init__(self, credentials: Optional[SlackCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the slack remove operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running slack remove operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running slack remove operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the slack remove operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
