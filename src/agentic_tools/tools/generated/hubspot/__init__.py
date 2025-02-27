# hubspot toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_hubspot_tools() -> List[BaseTool]:
    """Get all hubspot tools."""
    from . import operations
    return operations.get_tools()

class HubspotCredentials(BaseModel):
    """Credentials for hubspot authentication."""
    hubspot_api: Optional[Dict[str, Any]] = Field(None, description="hubspotApi")
    hubspot_app_token: Optional[Dict[str, Any]] = Field(None, description="hubspotAppToken")
    hubspot_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="hubspotOAuth2Api")

class HubspotToolkit(AgenticHubToolkit):
    """Toolkit for interacting with hubspot."""

    def __init__(self, credentials: Optional[HubspotCredentials] = None):
        """Initialize the hubspot toolkit with optional credentials.

        Args:
            credentials: HubspotCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all hubspot tools with the configured credentials."""
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
        """Get all hubspot tools with default credentials."""
        return get_hubspot_tools()
