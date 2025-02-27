# twake toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_twake_tools() -> List[BaseTool]:
    """Get all twake tools."""
    from . import operations
    return operations.get_tools()

class TwakeCredentials(BaseModel):
    """Credentials for twake authentication."""
    twake_cloud_api: Optional[Dict[str, Any]] = Field(None, description="twakeCloudApi")

class TwakeToolkit(AgenticHubToolkit):
    """Toolkit for interacting with twake."""

    def __init__(self, credentials: Optional[TwakeCredentials] = None):
        """Initialize the twake toolkit with optional credentials.

        Args:
            credentials: TwakeCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all twake tools with the configured credentials."""
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
        """Get all twake tools with default credentials."""
        return get_twake_tools()
