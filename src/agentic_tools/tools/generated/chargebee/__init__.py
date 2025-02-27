# chargebee toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_chargebee_tools() -> List[BaseTool]:
    """Get all chargebee tools."""
    from . import operations
    return operations.get_tools()

class ChargebeeCredentials(BaseModel):
    """Credentials for chargebee authentication."""
    chargebee_api: Optional[Dict[str, Any]] = Field(None, description="chargebeeApi")

class ChargebeeToolkit(AgenticHubToolkit):
    """Toolkit for interacting with chargebee."""

    def __init__(self, credentials: Optional[ChargebeeCredentials] = None):
        """Initialize the chargebee toolkit with optional credentials.

        Args:
            credentials: ChargebeeCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all chargebee tools with the configured credentials."""
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
        """Get all chargebee tools with default credentials."""
        return get_chargebee_tools()
