# youtube toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_youtube_tools() -> List[BaseTool]:
    """Get all youtube tools."""
    from . import operations
    return operations.get_tools()

class YoutubeCredentials(BaseModel):
    """Credentials for youtube authentication."""
    you_tube_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="youTubeOAuth2Api")

class YoutubeToolkit(AgenticHubToolkit):
    """Toolkit for interacting with youtube."""

    def __init__(self, credentials: Optional[YoutubeCredentials] = None):
        """Initialize the youtube toolkit with optional credentials.

        Args:
            credentials: YoutubeCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all youtube tools with the configured credentials."""
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
        """Get all youtube tools with default credentials."""
        return get_youtube_tools()
