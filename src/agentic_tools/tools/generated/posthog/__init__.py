# posthog toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_posthog_tools() -> List[BaseTool]:
    """Get all posthog tools."""
    from . import operations
    return operations.get_tools()

class PosthogCredentials(BaseModel):
    """Credentials for posthog authentication."""
    post_hog_api: Optional[Dict[str, Any]] = Field(None, description="postHogApi")

class PosthogToolkit(AgenticHubToolkit):
    """Toolkit for interacting with posthog."""

    def __init__(self, credentials: Optional[PosthogCredentials] = None):
        """Initialize the posthog toolkit with optional credentials.

        Args:
            credentials: PosthogCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all posthog tools with the configured credentials."""
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
        """Get all posthog tools with default credentials."""
        return get_posthog_tools()
