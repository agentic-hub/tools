# box toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_box_tools() -> List[BaseTool]:
    """Get all box tools."""
    from . import operations
    return operations.get_tools()

class BoxCredentials(BaseModel):
    """Credentials for box authentication."""
    box_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="boxOAuth2Api")

class BoxToolkit(AgenticHubToolkit):
    """Toolkit for interacting with box."""

    def __init__(self, credentials: Optional[BoxCredentials] = None):
        """Initialize the box toolkit with optional credentials.

        Args:
            credentials: BoxCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all box tools with the configured credentials."""
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
        """Get all box tools with default credentials."""
        return get_box_tools()
