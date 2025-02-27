# vonage toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_vonage_tools() -> List[BaseTool]:
    """Get all vonage tools."""
    from . import operations
    return operations.get_tools()

class VonageCredentials(BaseModel):
    """Credentials for vonage authentication."""
    vonage_api: Optional[Dict[str, Any]] = Field(None, description="vonageApi")

class VonageToolkit(AgenticHubToolkit):
    """Toolkit for interacting with vonage."""

    def __init__(self, credentials: Optional[VonageCredentials] = None):
        """Initialize the vonage toolkit with optional credentials.

        Args:
            credentials: VonageCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all vonage tools with the configured credentials."""
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
        """Get all vonage tools with default credentials."""
        return get_vonage_tools()
