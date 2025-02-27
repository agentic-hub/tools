# zoom toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_zoom_tools() -> List[BaseTool]:
    """Get all zoom tools."""
    from . import operations
    return operations.get_tools()

class ZoomCredentials(BaseModel):
    """Credentials for zoom authentication."""
    zoom_api: Optional[Dict[str, Any]] = Field(None, description="zoomApi")
    zoom_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="zoomOAuth2Api")

class ZoomToolkit(AgenticHubToolkit):
    """Toolkit for interacting with zoom."""

    def __init__(self, credentials: Optional[ZoomCredentials] = None):
        """Initialize the zoom toolkit with optional credentials.

        Args:
            credentials: ZoomCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all zoom tools with the configured credentials."""
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
        """Get all zoom tools with default credentials."""
        return get_zoom_tools()
