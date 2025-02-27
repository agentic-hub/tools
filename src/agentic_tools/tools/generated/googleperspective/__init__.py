# googleperspective toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googleperspective_tools() -> List[BaseTool]:
    """Get all googleperspective tools."""
    from . import operations
    return operations.get_tools()

class GoogleperspectiveCredentials(BaseModel):
    """Credentials for googleperspective authentication."""
    google_perspective_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googlePerspectiveOAuth2Api")

class GoogleperspectiveToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googleperspective."""

    def __init__(self, credentials: Optional[GoogleperspectiveCredentials] = None):
        """Initialize the googleperspective toolkit with optional credentials.

        Args:
            credentials: GoogleperspectiveCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googleperspective tools with the configured credentials."""
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
        """Get all googleperspective tools with default credentials."""
        return get_googleperspective_tools()
