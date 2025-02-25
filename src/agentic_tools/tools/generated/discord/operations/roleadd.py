from langchain.tools import BaseTool
from agentic_tools.tools.base.BaseTool import BaseModel, Field
from typing import Optional, Dict, Any, List, Union

class DiscordCredentials(BaseModel):
    """Credentials for discord authentication."""
    discord_bot_api: Optional[Dict[str, Any]] = Field(None, description="discordBotApi")
    discord_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="discordOAuth2Api")
    discord_webhook_api: Optional[Dict[str, Any]] = Field(None, description="discordWebhookApi")

class DiscordRoleaddToolInput(BaseModel):
    # Allow users to provide their own credentials
    credentials: Optional[DiscordCredentials] = Field(None, description="Custom credentials for authentication")
    content: Optional[str] = Field(None, description="The content of the message (up to 2000 characters)")
    files: Optional[Dict[str, Any]] = Field(None, description="Files")
    role: Optional[str] = Field(None, description="role")
    channel_id: Optional[Dict[str, Any]] = Field(None, description="Select the channel by name, URL, or ID")
    guild_id: Optional[Dict[str, Any]] = Field(None, description="Select the server (guild) that your bot is connected to")
    user_id: Optional[Dict[str, Any]] = Field(None, description="Select the user you want to assign a role to")
    return_all: Optional[bool] = Field(None, description="Whether to return all results or only up to a given limit")
    embeds: Optional[Dict[str, Any]] = Field(None, description="Embeds")
    operation: Optional[str] = Field(None, description="Operation")
    name: Optional[str] = Field(None, description="The name of the channel")
    limit: Optional[float] = Field(None, description="Max number of results to return")
    options: Optional[Dict[str, Any]] = Field(None, description="Options")
    message_id: Optional[str] = Field(None, description="The ID of the message")
    resource: Optional[str] = Field(None, description="Resource")
    authentication: Optional[str] = Field(None, description="Connection Type")


class DiscordRoleaddTool(BaseTool):
    name = "discord_roleadd"
    description = "Tool for discord roleAdd operation - roleAdd operation"
    
    def __init__(self, credentials: Optional[DiscordCredentials] = None, **kwargs):
        """Initialize the tool with optional custom credentials.
        
        Args:
            credentials: Credentials for authentication
            **kwargs: Additional keyword arguments
        """
        super().__init__(**kwargs)
        self.credentials = credentials
    
    def _run(self, **kwargs):
        """Run the discord roleAdd operation."""
        # Extract credentials if provided in the run arguments
        run_credentials = kwargs.pop("credentials", None)
        
        # Use run-time credentials if provided, otherwise use the ones from initialization
        credentials = run_credentials or self.credentials
        
        # Implement the tool logic here
        if credentials:
            # Create a safe copy of credentials for logging (hide sensitive values)
            safe_credentials = "{...}"  # Just indicate credentials are present
            return f"Running discord roleAdd operation with custom credentials {safe_credentials} and args: {kwargs}"
        else:
            return f"Running discord roleAdd operation with default credentials and args: {kwargs}"
    
    async def _arun(self, **kwargs):
        """Run the discord roleAdd operation asynchronously."""
        # Implement the async tool logic here
        return self._run(**kwargs)
