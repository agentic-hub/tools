# gotify toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_gotify_tools() -> List[BaseTool]:
    """Get all gotify tools."""
    from . import operations
    return operations.get_tools()

class GotifyCredentials(BaseModel):
    """Credentials for gotify authentication."""
    gotify_api: Optional[Dict[str, Any]] = Field(None, description="gotifyApi")

class GotifyToolkit(AgenticHubToolkit):
    """Toolkit for interacting with gotify."""

    def __init__(self, credentials: Optional[GotifyCredentials] = None):
        """Initialize the gotify toolkit with optional credentials.

        Args:
            credentials: GotifyCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all gotify tools with the configured credentials."""
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
        """Get all gotify tools with default credentials."""
        return get_gotify_tools()
