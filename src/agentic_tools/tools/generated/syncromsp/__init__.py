# syncromsp toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_syncromsp_tools() -> List[BaseTool]:
    """Get all syncromsp tools."""
    from . import operations
    return operations.get_tools()

class SyncromspCredentials(BaseModel):
    """Credentials for syncromsp authentication."""
    syncro_msp_api: Optional[Dict[str, Any]] = Field(None, description="syncroMspApi")

class SyncromspToolkit(AgenticHubToolkit):
    """Toolkit for interacting with syncromsp."""

    def __init__(self, credentials: Optional[SyncromspCredentials] = None):
        """Initialize the syncromsp toolkit with optional credentials.

        Args:
            credentials: SyncromspCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all syncromsp tools with the configured credentials."""
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
        """Get all syncromsp tools with default credentials."""
        return get_syncromsp_tools()
