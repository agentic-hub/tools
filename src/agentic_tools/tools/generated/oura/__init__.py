# oura toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_oura_tools() -> List[BaseTool]:
    """Get all oura tools."""
    from . import operations
    return operations.get_tools()

class OuraCredentials(BaseModel):
    """Credentials for oura authentication."""
    oura_api: Optional[Dict[str, Any]] = Field(None, description="ouraApi")

class OuraToolkit(AgenticHubToolkit):
    """Toolkit for interacting with oura."""

    def __init__(self, credentials: Optional[OuraCredentials] = None):
        """Initialize the oura toolkit with optional credentials.

        Args:
            credentials: OuraCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all oura tools with the configured credentials."""
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
        """Get all oura tools with default credentials."""
        return get_oura_tools()
