# freshdesk toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_freshdesk_tools() -> List[BaseTool]:
    """Get all freshdesk tools."""
    from . import operations
    return operations.get_tools()

class FreshdeskCredentials(BaseModel):
    """Credentials for freshdesk authentication."""
    freshdesk_api: Optional[Dict[str, Any]] = Field(None, description="freshdeskApi")

class FreshdeskToolkit(AgenticHubToolkit):
    """Toolkit for interacting with freshdesk."""

    def __init__(self, credentials: Optional[FreshdeskCredentials] = None):
        """Initialize the freshdesk toolkit with optional credentials.

        Args:
            credentials: FreshdeskCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all freshdesk tools with the configured credentials."""
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
        """Get all freshdesk tools with default credentials."""
        return get_freshdesk_tools()
