# webflow toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_webflow_tools() -> List[BaseTool]:
    """Get all webflow tools."""
    from . import operations
    return operations.get_tools()

class WebflowCredentials(BaseModel):
    """Credentials for webflow authentication."""
    webflow_api: Optional[Dict[str, Any]] = Field(None, description="webflowApi")
    webflow_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="webflowOAuth2Api")

class WebflowToolkit(AgenticHubToolkit):
    """Toolkit for interacting with webflow."""

    def __init__(self, credentials: Optional[WebflowCredentials] = None):
        """Initialize the webflow toolkit with optional credentials.

        Args:
            credentials: WebflowCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all webflow tools with the configured credentials."""
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
        """Get all webflow tools with default credentials."""
        return get_webflow_tools()
