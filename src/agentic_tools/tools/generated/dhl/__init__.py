# dhl toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_dhl_tools() -> List[BaseTool]:
    """Get all dhl tools."""
    from . import operations
    return operations.get_tools()

class DhlCredentials(BaseModel):
    """Credentials for dhl authentication."""
    dhl_api: Optional[Dict[str, Any]] = Field(None, description="dhlApi")

class DhlToolkit(AgenticHubToolkit):
    """Toolkit for interacting with dhl."""

    def __init__(self, credentials: Optional[DhlCredentials] = None):
        """Initialize the dhl toolkit with optional credentials.

        Args:
            credentials: DhlCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all dhl tools with the configured credentials."""
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
        """Get all dhl tools with default credentials."""
        return get_dhl_tools()
