from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MattermostCredentials(BaseModel):
    """Credentials for mattermost authentication."""
    mattermost_api: Optional[Dict[str, Any]] = Field(None, description="mattermostApi")

class MattermostPostToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MattermostCredentials] = Field(None, description="Custom credentials for authentication")
    post_id: Optional[str] = Field(None, description="ID of the post to delete")
    emoji_name: Optional[str] = Field(None, description="Emoji to use for this reaction")
    team_id: Optional[str] = Field(None, description="The Mattermost Team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    channel_id: Optional[str] = Field(None, description="The ID of the channel to post to. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    user_id: Optional[str] = Field(None, description="The ID of the user to invite into channel. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    other_options: Optional[Dict[str, Any]] = Field(None, description="Other options to set")
    operation: Optional[str] = Field(None, description="Operation")
    attachments: Optional[List[Any]] = Field(None, description="The attachment to add")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    message: Optional[str] = Field(None, description="The text to send")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class MattermostPostTool(BaseTool):
    name = "mattermost_post"
    description = "Tool for mattermost post operation - post operation"
    
    def __init__(self, credentials: Optional[MattermostCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mattermost post operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mattermost post operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mattermost post operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mattermost post operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
