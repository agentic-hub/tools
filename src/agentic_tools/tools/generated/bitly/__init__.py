# bitly toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_bitly_tools() -> List[BaseTool]:
    """Get all bitly tools."""
    from . import operations
    return operations.get_tools()

class BitlyCredentials(BaseModel):
    """Credentials for bitly authentication."""
    bitly_api: Optional[Dict[str, Any]] = Field(None, description="bitlyApi")
    bitly_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="bitlyOAuth2Api")

class BitlyToolkit(AgenticHubToolkit):
    """Toolkit for interacting with bitly."""

    def __init__(self, credentials: Optional[BitlyCredentials] = None):
        """Initialize the bitly toolkit with optional credentials.

        Args:
            credentials: BitlyCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all bitly tools with the configured credentials."""
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
        """Get all bitly tools with default credentials."""
        return get_bitly_tools()
