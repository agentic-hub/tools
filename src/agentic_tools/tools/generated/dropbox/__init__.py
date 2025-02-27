# dropbox toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_dropbox_tools() -> List[BaseTool]:
    """Get all dropbox tools."""
    from . import operations
    return operations.get_tools()

class DropboxCredentials(BaseModel):
    """Credentials for dropbox authentication."""
    dropbox_api: Optional[Dict[str, Any]] = Field(None, description="dropboxApi")
    dropbox_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="dropboxOAuth2Api")

class DropboxToolkit(AgenticHubToolkit):
    """Toolkit for interacting with dropbox."""

    def __init__(self, credentials: Optional[DropboxCredentials] = None):
        """Initialize the dropbox toolkit with optional credentials.

        Args:
            credentials: DropboxCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all dropbox tools with the configured credentials."""
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
        """Get all dropbox tools with default credentials."""
        return get_dropbox_tools()
