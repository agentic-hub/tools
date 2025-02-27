# mattermost toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mattermost_tools() -> List[BaseTool]:
    """Get all mattermost tools."""
    from . import operations
    return operations.get_tools()

class MattermostCredentials(BaseModel):
    """Credentials for mattermost authentication."""
    mattermost_api: Optional[Dict[str, Any]] = Field(None, description="mattermostApi")

class MattermostToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mattermost."""

    def __init__(self, credentials: Optional[MattermostCredentials] = None):
        """Initialize the mattermost toolkit with optional credentials.

        Args:
            credentials: MattermostCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mattermost tools with the configured credentials."""
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
        """Get all mattermost tools with default credentials."""
        return get_mattermost_tools()
