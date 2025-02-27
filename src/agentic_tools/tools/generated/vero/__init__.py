# vero toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_vero_tools() -> List[BaseTool]:
    """Get all vero tools."""
    from . import operations
    return operations.get_tools()

class VeroCredentials(BaseModel):
    """Credentials for vero authentication."""
    vero_api: Optional[Dict[str, Any]] = Field(None, description="veroApi")

class VeroToolkit(AgenticHubToolkit):
    """Toolkit for interacting with vero."""

    def __init__(self, credentials: Optional[VeroCredentials] = None):
        """Initialize the vero toolkit with optional credentials.

        Args:
            credentials: VeroCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all vero tools with the configured credentials."""
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
        """Get all vero tools with default credentials."""
        return get_vero_tools()
