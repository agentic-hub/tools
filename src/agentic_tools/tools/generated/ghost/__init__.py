# ghost toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_ghost_tools() -> List[BaseTool]:
    """Get all ghost tools."""
    from . import operations
    return operations.get_tools()

class GhostCredentials(BaseModel):
    """Credentials for ghost authentication."""
    ghost_admin_api: Optional[Dict[str, Any]] = Field(None, description="ghostAdminApi")
    ghost_content_api: Optional[Dict[str, Any]] = Field(None, description="ghostContentApi")

class GhostToolkit(AgenticHubToolkit):
    """Toolkit for interacting with ghost."""

    def __init__(self, credentials: Optional[GhostCredentials] = None):
        """Initialize the ghost toolkit with optional credentials.

        Args:
            credentials: GhostCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all ghost tools with the configured credentials."""
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
        """Get all ghost tools with default credentials."""
        return get_ghost_tools()
