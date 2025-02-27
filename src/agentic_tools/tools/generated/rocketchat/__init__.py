# rocketchat toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_rocketchat_tools() -> List[BaseTool]:
    """Get all rocketchat tools."""
    from . import operations
    return operations.get_tools()

class RocketchatCredentials(BaseModel):
    """Credentials for rocketchat authentication."""
    rocketchat_api: Optional[Dict[str, Any]] = Field(None, description="rocketchatApi")

class RocketchatToolkit(AgenticHubToolkit):
    """Toolkit for interacting with rocketchat."""

    def __init__(self, credentials: Optional[RocketchatCredentials] = None):
        """Initialize the rocketchat toolkit with optional credentials.

        Args:
            credentials: RocketchatCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all rocketchat tools with the configured credentials."""
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
        """Get all rocketchat tools with default credentials."""
        return get_rocketchat_tools()
