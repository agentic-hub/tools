# peekalink toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_peekalink_tools() -> List[BaseTool]:
    """Get all peekalink tools."""
    from . import operations
    return operations.get_tools()

class PeekalinkCredentials(BaseModel):
    """Credentials for peekalink authentication."""
    peekalink_api: Optional[Dict[str, Any]] = Field(None, description="peekalinkApi")

class PeekalinkToolkit(AgenticHubToolkit):
    """Toolkit for interacting with peekalink."""

    def __init__(self, credentials: Optional[PeekalinkCredentials] = None):
        """Initialize the peekalink toolkit with optional credentials.

        Args:
            credentials: PeekalinkCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all peekalink tools with the configured credentials."""
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
        """Get all peekalink tools with default credentials."""
        return get_peekalink_tools()
