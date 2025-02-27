# npm toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_npm_tools() -> List[BaseTool]:
    """Get all npm tools."""
    from . import operations
    return operations.get_tools()

class NpmCredentials(BaseModel):
    """Credentials for npm authentication."""
    npm_api: Optional[Dict[str, Any]] = Field(None, description="npmApi")

class NpmToolkit(AgenticHubToolkit):
    """Toolkit for interacting with npm."""

    def __init__(self, credentials: Optional[NpmCredentials] = None):
        """Initialize the npm toolkit with optional credentials.

        Args:
            credentials: NpmCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all npm tools with the configured credentials."""
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
        """Get all npm tools with default credentials."""
        return get_npm_tools()
