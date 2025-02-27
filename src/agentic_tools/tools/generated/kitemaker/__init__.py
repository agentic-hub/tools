# kitemaker toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_kitemaker_tools() -> List[BaseTool]:
    """Get all kitemaker tools."""
    from . import operations
    return operations.get_tools()

class KitemakerCredentials(BaseModel):
    """Credentials for kitemaker authentication."""
    kitemaker_api: Optional[Dict[str, Any]] = Field(None, description="kitemakerApi")

class KitemakerToolkit(AgenticHubToolkit):
    """Toolkit for interacting with kitemaker."""

    def __init__(self, credentials: Optional[KitemakerCredentials] = None):
        """Initialize the kitemaker toolkit with optional credentials.

        Args:
            credentials: KitemakerCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all kitemaker tools with the configured credentials."""
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
        """Get all kitemaker tools with default credentials."""
        return get_kitemaker_tools()
