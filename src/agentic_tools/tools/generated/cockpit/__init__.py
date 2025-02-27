# cockpit toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_cockpit_tools() -> List[BaseTool]:
    """Get all cockpit tools."""
    from . import operations
    return operations.get_tools()

class CockpitCredentials(BaseModel):
    """Credentials for cockpit authentication."""
    cockpit_api: Optional[Dict[str, Any]] = Field(None, description="cockpitApi")

class CockpitToolkit(AgenticHubToolkit):
    """Toolkit for interacting with cockpit."""

    def __init__(self, credentials: Optional[CockpitCredentials] = None):
        """Initialize the cockpit toolkit with optional credentials.

        Args:
            credentials: CockpitCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all cockpit tools with the configured credentials."""
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
        """Get all cockpit tools with default credentials."""
        return get_cockpit_tools()
