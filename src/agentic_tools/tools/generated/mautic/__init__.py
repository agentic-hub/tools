# mautic toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mautic_tools() -> List[BaseTool]:
    """Get all mautic tools."""
    from . import operations
    return operations.get_tools()

class MauticCredentials(BaseModel):
    """Credentials for mautic authentication."""
    mautic_api: Optional[Dict[str, Any]] = Field(None, description="mauticApi")
    mautic_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="mauticOAuth2Api")

class MauticToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mautic."""

    def __init__(self, credentials: Optional[MauticCredentials] = None):
        """Initialize the mautic toolkit with optional credentials.

        Args:
            credentials: MauticCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mautic tools with the configured credentials."""
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
        """Get all mautic tools with default credentials."""
        return get_mautic_tools()
