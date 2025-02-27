# iterable toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_iterable_tools() -> List[BaseTool]:
    """Get all iterable tools."""
    from . import operations
    return operations.get_tools()

class IterableCredentials(BaseModel):
    """Credentials for iterable authentication."""
    iterable_api: Optional[Dict[str, Any]] = Field(None, description="iterableApi")

class IterableToolkit(AgenticHubToolkit):
    """Toolkit for interacting with iterable."""

    def __init__(self, credentials: Optional[IterableCredentials] = None):
        """Initialize the iterable toolkit with optional credentials.

        Args:
            credentials: IterableCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all iterable tools with the configured credentials."""
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
        """Get all iterable tools with default credentials."""
        return get_iterable_tools()
