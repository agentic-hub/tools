# hunter toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_hunter_tools() -> List[BaseTool]:
    """Get all hunter tools."""
    from . import operations
    return operations.get_tools()

class HunterCredentials(BaseModel):
    """Credentials for hunter authentication."""
    hunter_api: Optional[Dict[str, Any]] = Field(None, description="hunterApi")

class HunterToolkit(AgenticHubToolkit):
    """Toolkit for interacting with hunter."""

    def __init__(self, credentials: Optional[HunterCredentials] = None):
        """Initialize the hunter toolkit with optional credentials.

        Args:
            credentials: HunterCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all hunter tools with the configured credentials."""
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
        """Get all hunter tools with default credentials."""
        return get_hunter_tools()
