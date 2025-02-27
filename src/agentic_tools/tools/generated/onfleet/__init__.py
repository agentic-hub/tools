# onfleet toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_onfleet_tools() -> List[BaseTool]:
    """Get all onfleet tools."""
    from . import operations
    return operations.get_tools()

class OnfleetCredentials(BaseModel):
    """Credentials for onfleet authentication."""
    onfleet_api: Optional[Dict[str, Any]] = Field(None, description="onfleetApi")

class OnfleetToolkit(AgenticHubToolkit):
    """Toolkit for interacting with onfleet."""

    def __init__(self, credentials: Optional[OnfleetCredentials] = None):
        """Initialize the onfleet toolkit with optional credentials.

        Args:
            credentials: OnfleetCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all onfleet tools with the configured credentials."""
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
        """Get all onfleet tools with default credentials."""
        return get_onfleet_tools()
