# actionnetwork toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_actionnetwork_tools() -> List[BaseTool]:
    """Get all actionnetwork tools."""
    from . import operations
    return operations.get_tools()

class ActionnetworkCredentials(BaseModel):
    """Credentials for actionnetwork authentication."""
    action_network_api: Optional[Dict[str, Any]] = Field(None, description="actionNetworkApi")

class ActionnetworkToolkit(AgenticHubToolkit):
    """Toolkit for interacting with actionnetwork."""

    def __init__(self, credentials: Optional[ActionnetworkCredentials] = None):
        """Initialize the actionnetwork toolkit with optional credentials.

        Args:
            credentials: ActionnetworkCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all actionnetwork tools with the configured credentials."""
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
        """Get all actionnetwork tools with default credentials."""
        return get_actionnetwork_tools()
