# awssns toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_awssns_tools() -> List[BaseTool]:
    """Get all awssns tools."""
    from . import operations
    return operations.get_tools()

class AwssnsCredentials(BaseModel):
    """Credentials for awssns authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwsSnsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with awssns."""

    def __init__(self, credentials: Optional[AwssnsCredentials] = None):
        """Initialize the awssns toolkit with optional credentials.

        Args:
            credentials: AwssnsCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all awssns tools with the configured credentials."""
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
        """Get all awssns tools with default credentials."""
        return get_awssns_tools()
