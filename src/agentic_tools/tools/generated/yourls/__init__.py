# yourls toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_yourls_tools() -> List[BaseTool]:
    """Get all yourls tools."""
    from . import operations
    return operations.get_tools()

class YourlsCredentials(BaseModel):
    """Credentials for yourls authentication."""
    yourls_api: Optional[Dict[str, Any]] = Field(None, description="yourlsApi")

class YourlsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with yourls."""

    def __init__(self, credentials: Optional[YourlsCredentials] = None):
        """Initialize the yourls toolkit with optional credentials.

        Args:
            credentials: YourlsCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all yourls tools with the configured credentials."""
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
        """Get all yourls tools with default credentials."""
        return get_yourls_tools()
