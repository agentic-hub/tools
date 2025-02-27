# wekan toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_wekan_tools() -> List[BaseTool]:
    """Get all wekan tools."""
    from . import operations
    return operations.get_tools()

class WekanCredentials(BaseModel):
    """Credentials for wekan authentication."""
    wekan_api: Optional[Dict[str, Any]] = Field(None, description="wekanApi")

class WekanToolkit(AgenticHubToolkit):
    """Toolkit for interacting with wekan."""

    def __init__(self, credentials: Optional[WekanCredentials] = None):
        """Initialize the wekan toolkit with optional credentials.

        Args:
            credentials: WekanCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all wekan tools with the configured credentials."""
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
        """Get all wekan tools with default credentials."""
        return get_wekan_tools()
