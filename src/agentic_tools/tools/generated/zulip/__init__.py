# zulip toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_zulip_tools() -> List[BaseTool]:
    """Get all zulip tools."""
    from . import operations
    return operations.get_tools()

class ZulipCredentials(BaseModel):
    """Credentials for zulip authentication."""
    zulip_api: Optional[Dict[str, Any]] = Field(None, description="zulipApi")

class ZulipToolkit(AgenticHubToolkit):
    """Toolkit for interacting with zulip."""

    def __init__(self, credentials: Optional[ZulipCredentials] = None):
        """Initialize the zulip toolkit with optional credentials.

        Args:
            credentials: ZulipCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all zulip tools with the configured credentials."""
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
        """Get all zulip tools with default credentials."""
        return get_zulip_tools()
