# zohocrm toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_zohocrm_tools() -> List[BaseTool]:
    """Get all zohocrm tools."""
    from . import operations
    return operations.get_tools()

class ZohocrmCredentials(BaseModel):
    """Credentials for zohocrm authentication."""
    zoho_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="zohoOAuth2Api")

class ZohocrmToolkit(AgenticHubToolkit):
    """Toolkit for interacting with zohocrm."""

    def __init__(self, credentials: Optional[ZohocrmCredentials] = None):
        """Initialize the zohocrm toolkit with optional credentials.

        Args:
            credentials: ZohocrmCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all zohocrm tools with the configured credentials."""
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
        """Get all zohocrm tools with default credentials."""
        return get_zohocrm_tools()
