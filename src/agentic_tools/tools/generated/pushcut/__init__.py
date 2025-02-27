# pushcut toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_pushcut_tools() -> List[BaseTool]:
    """Get all pushcut tools."""
    from . import operations
    return operations.get_tools()

class PushcutCredentials(BaseModel):
    """Credentials for pushcut authentication."""
    pushcut_api: Optional[Dict[str, Any]] = Field(None, description="pushcutApi")

class PushcutToolkit(AgenticHubToolkit):
    """Toolkit for interacting with pushcut."""

    def __init__(self, credentials: Optional[PushcutCredentials] = None):
        """Initialize the pushcut toolkit with optional credentials.

        Args:
            credentials: PushcutCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all pushcut tools with the configured credentials."""
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
        """Get all pushcut tools with default credentials."""
        return get_pushcut_tools()
