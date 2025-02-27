# freshworkscrm toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_freshworkscrm_tools() -> List[BaseTool]:
    """Get all freshworkscrm tools."""
    from . import operations
    return operations.get_tools()

class FreshworkscrmCredentials(BaseModel):
    """Credentials for freshworkscrm authentication."""
    freshworks_crm_api: Optional[Dict[str, Any]] = Field(None, description="freshworksCrmApi")

class FreshworkscrmToolkit(AgenticHubToolkit):
    """Toolkit for interacting with freshworkscrm."""

    def __init__(self, credentials: Optional[FreshworkscrmCredentials] = None):
        """Initialize the freshworkscrm toolkit with optional credentials.

        Args:
            credentials: FreshworkscrmCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all freshworkscrm tools with the configured credentials."""
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
        """Get all freshworkscrm tools with default credentials."""
        return get_freshworkscrm_tools()
