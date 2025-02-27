# gsuiteadmin toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_gsuiteadmin_tools() -> List[BaseTool]:
    """Get all gsuiteadmin tools."""
    from . import operations
    return operations.get_tools()

class GsuiteadminCredentials(BaseModel):
    """Credentials for gsuiteadmin authentication."""
    g_suite_admin_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="gSuiteAdminOAuth2Api")

class GsuiteadminToolkit(AgenticHubToolkit):
    """Toolkit for interacting with gsuiteadmin."""

    def __init__(self, credentials: Optional[GsuiteadminCredentials] = None):
        """Initialize the gsuiteadmin toolkit with optional credentials.

        Args:
            credentials: GsuiteadminCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all gsuiteadmin tools with the configured credentials."""
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
        """Get all gsuiteadmin tools with default credentials."""
        return get_gsuiteadmin_tools()
