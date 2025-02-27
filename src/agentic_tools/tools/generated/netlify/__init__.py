# netlify toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_netlify_tools() -> List[BaseTool]:
    """Get all netlify tools."""
    from . import operations
    return operations.get_tools()

class NetlifyCredentials(BaseModel):
    """Credentials for netlify authentication."""
    netlify_api: Optional[Dict[str, Any]] = Field(None, description="netlifyApi")

class NetlifyToolkit(AgenticHubToolkit):
    """Toolkit for interacting with netlify."""

    def __init__(self, credentials: Optional[NetlifyCredentials] = None):
        """Initialize the netlify toolkit with optional credentials.

        Args:
            credentials: NetlifyCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all netlify tools with the configured credentials."""
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
        """Get all netlify tools with default credentials."""
        return get_netlify_tools()
