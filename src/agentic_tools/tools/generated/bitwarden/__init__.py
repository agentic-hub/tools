# bitwarden toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_bitwarden_tools() -> List[BaseTool]:
    """Get all bitwarden tools."""
    from . import operations
    return operations.get_tools()

class BitwardenCredentials(BaseModel):
    """Credentials for bitwarden authentication."""
    bitwarden_api: Optional[Dict[str, Any]] = Field(None, description="bitwardenApi")

class BitwardenToolkit(AgenticHubToolkit):
    """Toolkit for interacting with bitwarden."""

    def __init__(self, credentials: Optional[BitwardenCredentials] = None):
        """Initialize the bitwarden toolkit with optional credentials.

        Args:
            credentials: BitwardenCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all bitwarden tools with the configured credentials."""
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
        """Get all bitwarden tools with default credentials."""
        return get_bitwarden_tools()
