# intercom toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_intercom_tools() -> List[BaseTool]:
    """Get all intercom tools."""
    from . import operations
    return operations.get_tools()

class IntercomCredentials(BaseModel):
    """Credentials for intercom authentication."""
    intercom_api: Optional[Dict[str, Any]] = Field(None, description="intercomApi")

class IntercomToolkit(AgenticHubToolkit):
    """Toolkit for interacting with intercom."""

    def __init__(self, credentials: Optional[IntercomCredentials] = None):
        """Initialize the intercom toolkit with optional credentials.

        Args:
            credentials: IntercomCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all intercom tools with the configured credentials."""
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
        """Get all intercom tools with default credentials."""
        return get_intercom_tools()
