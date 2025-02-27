# clickup toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_clickup_tools() -> List[BaseTool]:
    """Get all clickup tools."""
    from . import operations
    return operations.get_tools()

class ClickupCredentials(BaseModel):
    """Credentials for clickup authentication."""
    click_up_api: Optional[Dict[str, Any]] = Field(None, description="clickUpApi")
    click_up_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="clickUpOAuth2Api")

class ClickupToolkit(AgenticHubToolkit):
    """Toolkit for interacting with clickup."""

    def __init__(self, credentials: Optional[ClickupCredentials] = None):
        """Initialize the clickup toolkit with optional credentials.

        Args:
            credentials: ClickupCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all clickup tools with the configured credentials."""
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
        """Get all clickup tools with default credentials."""
        return get_clickup_tools()
