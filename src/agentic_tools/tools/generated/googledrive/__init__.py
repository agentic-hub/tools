# googledrive toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googledrive_tools() -> List[BaseTool]:
    """Get all googledrive tools."""
    from . import operations
    return operations.get_tools()

class GoogledriveCredentials(BaseModel):
    """Credentials for googledrive authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_drive_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleDriveOAuth2Api")

class GoogledriveToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googledrive."""

    def __init__(self, credentials: Optional[GoogledriveCredentials] = None):
        """Initialize the googledrive toolkit with optional credentials.

        Args:
            credentials: GoogledriveCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googledrive tools with the configured credentials."""
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
        """Get all googledrive tools with default credentials."""
        return get_googledrive_tools()
