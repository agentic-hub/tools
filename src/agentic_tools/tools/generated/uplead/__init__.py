# uplead toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_uplead_tools() -> List[BaseTool]:
    """Get all uplead tools."""
    from . import operations
    return operations.get_tools()

class UpleadCredentials(BaseModel):
    """Credentials for uplead authentication."""
    uplead_api: Optional[Dict[str, Any]] = Field(None, description="upleadApi")

class UpleadToolkit(AgenticHubToolkit):
    """Toolkit for interacting with uplead."""

    def __init__(self, credentials: Optional[UpleadCredentials] = None):
        """Initialize the uplead toolkit with optional credentials.

        Args:
            credentials: UpleadCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all uplead tools with the configured credentials."""
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
        """Get all uplead tools with default credentials."""
        return get_uplead_tools()
