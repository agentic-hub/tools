# discord toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_discord_tools() -> List[BaseTool]:
    """Get all discord tools."""
    from . import operations
    return operations.get_tools()

class DiscordCredentials(BaseModel):
    """Credentials for discord authentication."""
    discord_bot_api: Optional[Dict[str, Any]] = Field(None, description="discordBotApi")
    discord_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="discordOAuth2Api")
    discord_webhook_api: Optional[Dict[str, Any]] = Field(None, description="discordWebhookApi")

class DiscordToolkit(AgenticHubToolkit):
    """Toolkit for interacting with discord."""

    def __init__(self, credentials: Optional[DiscordCredentials] = None):
        """Initialize the discord toolkit with optional credentials.

        Args:
            credentials: DiscordCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all discord tools with the configured credentials."""
        from . import operations
        return self.get_tools_from_operations(operations)
        # Apply credentials to each tool if provided
        if self.credentials:
            for tool in tools:
                # Set credentials on each tool instance
                tool.credentials = self.credentials
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all discord tools with default credentials."""
        return get_discord_tools()
