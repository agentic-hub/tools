# stackby toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_stackby_tools() -> List[BaseTool]:
    """Get all stackby tools."""
    from . import operations
    return operations.get_tools()

class StackbyCredentials(BaseModel):
    """Credentials for stackby authentication."""
    stackby_api: Optional[Dict[str, Any]] = Field(None, description="stackbyApi")

class StackbyToolkit(AgenticHubToolkit):
    """Toolkit for interacting with stackby."""

    def __init__(self, credentials: Optional[StackbyCredentials] = None):
        """Initialize the stackby toolkit with optional credentials.

        Args:
            credentials: StackbyCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all stackby tools with the configured credentials."""
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
        """Get all stackby tools with default credentials."""
        return get_stackby_tools()
