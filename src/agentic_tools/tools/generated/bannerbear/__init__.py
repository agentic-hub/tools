# bannerbear toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_bannerbear_tools() -> List[BaseTool]:
    """Get all bannerbear tools."""
    from . import operations
    return operations.get_tools()

class BannerbearCredentials(BaseModel):
    """Credentials for bannerbear authentication."""
    bannerbear_api: Optional[Dict[str, Any]] = Field(None, description="bannerbearApi")

class BannerbearToolkit(AgenticHubToolkit):
    """Toolkit for interacting with bannerbear."""

    def __init__(self, credentials: Optional[BannerbearCredentials] = None):
        """Initialize the bannerbear toolkit with optional credentials.

        Args:
            credentials: BannerbearCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all bannerbear tools with the configured credentials."""
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
        """Get all bannerbear tools with default credentials."""
        return get_bannerbear_tools()
