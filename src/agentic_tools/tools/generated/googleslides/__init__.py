# googleslides toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googleslides_tools() -> List[BaseTool]:
    """Get all googleslides tools."""
    from . import operations
    return operations.get_tools()

class GoogleslidesCredentials(BaseModel):
    """Credentials for googleslides authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_slides_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleSlidesOAuth2Api")

class GoogleslidesToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googleslides."""

    def __init__(self, credentials: Optional[GoogleslidesCredentials] = None):
        """Initialize the googleslides toolkit with optional credentials.

        Args:
            credentials: GoogleslidesCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googleslides tools with the configured credentials."""
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
        """Get all googleslides tools with default credentials."""
        return get_googleslides_tools()
