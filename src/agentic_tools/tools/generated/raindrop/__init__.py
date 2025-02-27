# raindrop toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_raindrop_tools() -> List[BaseTool]:
    """Get all raindrop tools."""
    from . import operations
    return operations.get_tools()

class RaindropCredentials(BaseModel):
    """Credentials for raindrop authentication."""
    raindrop_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="raindropOAuth2Api")

class RaindropToolkit(AgenticHubToolkit):
    """Toolkit for interacting with raindrop."""

    def __init__(self, credentials: Optional[RaindropCredentials] = None):
        """Initialize the raindrop toolkit with optional credentials.

        Args:
            credentials: RaindropCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all raindrop tools with the configured credentials."""
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
        """Get all raindrop tools with default credentials."""
        return get_raindrop_tools()
