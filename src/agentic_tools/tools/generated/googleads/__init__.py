# googleads toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googleads_tools() -> List[BaseTool]:
    """Get all googleads tools."""
    from . import operations
    return operations.get_tools()

class GoogleadsCredentials(BaseModel):
    """Credentials for googleads authentication."""
    google_ads_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleAdsOAuth2Api")

class GoogleadsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googleads."""

    def __init__(self, credentials: Optional[GoogleadsCredentials] = None):
        """Initialize the googleads toolkit with optional credentials.

        Args:
            credentials: GoogleadsCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googleads tools with the configured credentials."""
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
        """Get all googleads tools with default credentials."""
        return get_googleads_tools()
