# mocean toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mocean_tools() -> List[BaseTool]:
    """Get all mocean tools."""
    from . import operations
    return operations.get_tools()

class MoceanCredentials(BaseModel):
    """Credentials for mocean authentication."""
    mocean_api: Optional[Dict[str, Any]] = Field(None, description="moceanApi")

class MoceanToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mocean."""

    def __init__(self, credentials: Optional[MoceanCredentials] = None):
        """Initialize the mocean toolkit with optional credentials.

        Args:
            credentials: MoceanCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mocean tools with the configured credentials."""
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
        """Get all mocean tools with default credentials."""
        return get_mocean_tools()
