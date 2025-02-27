# plivo toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_plivo_tools() -> List[BaseTool]:
    """Get all plivo tools."""
    from . import operations
    return operations.get_tools()

class PlivoCredentials(BaseModel):
    """Credentials for plivo authentication."""
    plivo_api: Optional[Dict[str, Any]] = Field(None, description="plivoApi")

class PlivoToolkit(AgenticHubToolkit):
    """Toolkit for interacting with plivo."""

    def __init__(self, credentials: Optional[PlivoCredentials] = None):
        """Initialize the plivo toolkit with optional credentials.

        Args:
            credentials: PlivoCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all plivo tools with the configured credentials."""
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
        """Get all plivo tools with default credentials."""
        return get_plivo_tools()
