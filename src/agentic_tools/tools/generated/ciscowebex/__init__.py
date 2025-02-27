# ciscowebex toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_ciscowebex_tools() -> List[BaseTool]:
    """Get all ciscowebex tools."""
    from . import operations
    return operations.get_tools()

class CiscowebexCredentials(BaseModel):
    """Credentials for ciscowebex authentication."""
    cisco_webex_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="ciscoWebexOAuth2Api")

class CiscowebexToolkit(AgenticHubToolkit):
    """Toolkit for interacting with ciscowebex."""

    def __init__(self, credentials: Optional[CiscowebexCredentials] = None):
        """Initialize the ciscowebex toolkit with optional credentials.

        Args:
            credentials: CiscowebexCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all ciscowebex tools with the configured credentials."""
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
        """Get all ciscowebex tools with default credentials."""
        return get_ciscowebex_tools()
