# googleanalytics toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googleanalytics_tools() -> List[BaseTool]:
    """Get all googleanalytics tools."""
    from . import operations
    return operations.get_tools()

class GoogleanalyticsCredentials(BaseModel):
    """Credentials for googleanalytics authentication."""
    google_analytics_o_auth2: Optional[Dict[str, Any]] = Field(None, description="googleAnalyticsOAuth2")

class GoogleanalyticsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googleanalytics."""

    def __init__(self, credentials: Optional[GoogleanalyticsCredentials] = None):
        """Initialize the googleanalytics toolkit with optional credentials.

        Args:
            credentials: GoogleanalyticsCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googleanalytics tools with the configured credentials."""
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
        """Get all googleanalytics tools with default credentials."""
        return get_googleanalytics_tools()
