# helpscout toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_helpscout_tools() -> List[BaseTool]:
    """Get all helpscout tools."""
    from . import operations
    return operations.get_tools()

class HelpscoutCredentials(BaseModel):
    """Credentials for helpscout authentication."""
    help_scout_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="helpScoutOAuth2Api")

class HelpscoutToolkit(AgenticHubToolkit):
    """Toolkit for interacting with helpscout."""

    def __init__(self, credentials: Optional[HelpscoutCredentials] = None):
        """Initialize the helpscout toolkit with optional credentials.

        Args:
            credentials: HelpscoutCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all helpscout tools with the configured credentials."""
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
        """Get all helpscout tools with default credentials."""
        return get_helpscout_tools()
