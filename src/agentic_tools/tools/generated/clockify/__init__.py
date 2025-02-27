# clockify toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_clockify_tools() -> List[BaseTool]:
    """Get all clockify tools."""
    from . import operations
    return operations.get_tools()

class ClockifyCredentials(BaseModel):
    """Credentials for clockify authentication."""
    clockify_api: Optional[Dict[str, Any]] = Field(None, description="clockifyApi")

class ClockifyToolkit(AgenticHubToolkit):
    """Toolkit for interacting with clockify."""

    def __init__(self, credentials: Optional[ClockifyCredentials] = None):
        """Initialize the clockify toolkit with optional credentials.

        Args:
            credentials: ClockifyCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all clockify tools with the configured credentials."""
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
        """Get all clockify tools with default credentials."""
        return get_clockify_tools()
