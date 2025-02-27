# gotowebinar toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_gotowebinar_tools() -> List[BaseTool]:
    """Get all gotowebinar tools."""
    from . import operations
    return operations.get_tools()

class GotowebinarCredentials(BaseModel):
    """Credentials for gotowebinar authentication."""
    go_to_webinar_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="goToWebinarOAuth2Api")

class GotowebinarToolkit(AgenticHubToolkit):
    """Toolkit for interacting with gotowebinar."""

    def __init__(self, credentials: Optional[GotowebinarCredentials] = None):
        """Initialize the gotowebinar toolkit with optional credentials.

        Args:
            credentials: GotowebinarCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all gotowebinar tools with the configured credentials."""
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
        """Get all gotowebinar tools with default credentials."""
        return get_gotowebinar_tools()
