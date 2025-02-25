from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class MattermostCredentials(BaseModel):
    """Credentials for mattermost authentication."""
    mattermost_api: Optional[Dict[str, Any]] = Field(None, description="mattermostApi")

class MattermostCreateToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[MattermostCredentials] = Field(None, description="Custom credentials for authentication")
    post_id: Optional[str] = Field(None, description="ID of the post to react to. Obtainable from the post link: <code>https://mattermost.internal.n8n.io/[server]/pl/[postId]</code>")
    emoji_name: Optional[str] = Field(None, description="Emoji to use for this reaction")
    team_id: Optional[str] = Field(None, description="The Mattermost Team. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    channel: Optional[str] = Field(None, description="The unique handle for the channel, will be present in the channel URL")
    display_name: Optional[str] = Field(None, description="The non-unique UI name for the channel")
    channel_id: Optional[str] = Field(None, description="The ID of the channel to soft delete. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    auth_service: Optional[str] = Field(None, description="Auth Service")
    auth_data: Optional[str] = Field(None, description="Auth Data")
    type: Optional[str] = Field(None, description="The type of channel to create")
    user_id: Optional[str] = Field(None, description="ID of the user sending the reaction. Choose from the list, or specify an ID using an <a href=\"https://docs.n8n.io/code-examples/expressions/\">expression</a>.")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    email: Optional[str] = Field(None, description="Email")
    password: Optional[str] = Field(None, description="The password used for email authentication")
    operation: Optional[str] = Field(None, description="Operation")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    message: Optional[str] = Field(None, description="The text to send")
    username: Optional[str] = Field(None, description="Username")
    resource: Optional[str] = Field(None, description="Resource")
    additional_fields: Optional[Dict[str, Any]] = Field(None, description="Additional Fields")


class MattermostCreateTool(BaseTool):
    name = "mattermost_create"
    description = "Tool for mattermost create operation - create operation"
    
    def __init__(self, credentials: Optional[MattermostCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the mattermost create operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running mattermost create operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running mattermost create operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the mattermost create operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
