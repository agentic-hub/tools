# asana toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_asana_tools() -> List[BaseTool]:
    """Get all asana tools."""
    from . import operations
    return operations.get_tools()

class AsanaCredentials(BaseModel):
    """Credentials for asana authentication."""
    asana_api: Optional[Dict[str, Any]] = Field(None, description="asanaApi")
    asana_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="asanaOAuth2Api")

class AsanaToolkit(AgenticHubToolkit):
    """Toolkit for interacting with asana."""

    def __init__(self, credentials: Optional[AsanaCredentials] = None):
        """Initialize the asana toolkit with optional credentials.

        Args:
            credentials: AsanaCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all asana tools with the configured credentials."""
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
        """Get all asana tools with default credentials."""
        return get_asana_tools()
