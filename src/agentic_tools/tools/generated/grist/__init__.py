# grist toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_grist_tools() -> List[BaseTool]:
    """Get all grist tools."""
    from . import operations
    return operations.get_tools()

class GristCredentials(BaseModel):
    """Credentials for grist authentication."""
    grist_api: Optional[Dict[str, Any]] = Field(None, description="gristApi")

class GristToolkit(AgenticHubToolkit):
    """Toolkit for interacting with grist."""

    def __init__(self, credentials: Optional[GristCredentials] = None):
        """Initialize the grist toolkit with optional credentials.

        Args:
            credentials: GristCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all grist tools with the configured credentials."""
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
        """Get all grist tools with default credentials."""
        return get_grist_tools()
