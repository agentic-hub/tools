# freshservice toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_freshservice_tools() -> List[BaseTool]:
    """Get all freshservice tools."""
    from . import operations
    return operations.get_tools()

class FreshserviceCredentials(BaseModel):
    """Credentials for freshservice authentication."""
    freshservice_api: Optional[Dict[str, Any]] = Field(None, description="freshserviceApi")

class FreshserviceToolkit(AgenticHubToolkit):
    """Toolkit for interacting with freshservice."""

    def __init__(self, credentials: Optional[FreshserviceCredentials] = None):
        """Initialize the freshservice toolkit with optional credentials.

        Args:
            credentials: FreshserviceCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all freshservice tools with the configured credentials."""
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
        """Get all freshservice tools with default credentials."""
        return get_freshservice_tools()
