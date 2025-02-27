# keap toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_keap_tools() -> List[BaseTool]:
    """Get all keap tools."""
    from . import operations
    return operations.get_tools()

class KeapCredentials(BaseModel):
    """Credentials for keap authentication."""
    keap_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="keapOAuth2Api")

class KeapToolkit(AgenticHubToolkit):
    """Toolkit for interacting with keap."""

    def __init__(self, credentials: Optional[KeapCredentials] = None):
        """Initialize the keap toolkit with optional credentials.

        Args:
            credentials: KeapCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all keap tools with the configured credentials."""
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
        """Get all keap tools with default credentials."""
        return get_keap_tools()
