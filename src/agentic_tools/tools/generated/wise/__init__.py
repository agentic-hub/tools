# wise toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_wise_tools() -> List[BaseTool]:
    """Get all wise tools."""
    from . import operations
    return operations.get_tools()

class WiseCredentials(BaseModel):
    """Credentials for wise authentication."""
    wise_api: Optional[Dict[str, Any]] = Field(None, description="wiseApi")

class WiseToolkit(AgenticHubToolkit):
    """Toolkit for interacting with wise."""

    def __init__(self, credentials: Optional[WiseCredentials] = None):
        """Initialize the wise toolkit with optional credentials.

        Args:
            credentials: WiseCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all wise tools with the configured credentials."""
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
        """Get all wise tools with default credentials."""
        return get_wise_tools()
