# spotify toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_spotify_tools() -> List[BaseTool]:
    """Get all spotify tools."""
    from . import operations
    return operations.get_tools()

class SpotifyCredentials(BaseModel):
    """Credentials for spotify authentication."""
    spotify_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="spotifyOAuth2Api")

class SpotifyToolkit(AgenticHubToolkit):
    """Toolkit for interacting with spotify."""

    def __init__(self, credentials: Optional[SpotifyCredentials] = None):
        """Initialize the spotify toolkit with optional credentials.

        Args:
            credentials: SpotifyCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all spotify tools with the configured credentials."""
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
        """Get all spotify tools with default credentials."""
        return get_spotify_tools()
