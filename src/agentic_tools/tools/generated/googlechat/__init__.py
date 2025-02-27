# googlechat toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googlechat_tools() -> List[BaseTool]:
    """Get all googlechat tools."""
    from . import operations
    return operations.get_tools()

class GooglechatCredentials(BaseModel):
    """Credentials for googlechat authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")

class GooglechatToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googlechat."""

    def __init__(self, credentials: Optional[GooglechatCredentials] = None):
        """Initialize the googlechat toolkit with optional credentials.

        Args:
            credentials: GooglechatCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googlechat tools with the configured credentials."""
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
        """Get all googlechat tools with default credentials."""
        return get_googlechat_tools()
