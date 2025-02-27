# xero toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_xero_tools() -> List[BaseTool]:
    """Get all xero tools."""
    from . import operations
    return operations.get_tools()

class XeroCredentials(BaseModel):
    """Credentials for xero authentication."""
    xero_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="xeroOAuth2Api")

class XeroToolkit(AgenticHubToolkit):
    """Toolkit for interacting with xero."""

    def __init__(self, credentials: Optional[XeroCredentials] = None):
        """Initialize the xero toolkit with optional credentials.

        Args:
            credentials: XeroCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all xero tools with the configured credentials."""
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
        """Get all xero tools with default credentials."""
        return get_xero_tools()
