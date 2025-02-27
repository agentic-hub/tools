# egoi toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_egoi_tools() -> List[BaseTool]:
    """Get all egoi tools."""
    from . import operations
    return operations.get_tools()

class EgoiCredentials(BaseModel):
    """Credentials for egoi authentication."""
    egoi_api: Optional[Dict[str, Any]] = Field(None, description="egoiApi")

class EgoiToolkit(AgenticHubToolkit):
    """Toolkit for interacting with egoi."""

    def __init__(self, credentials: Optional[EgoiCredentials] = None):
        """Initialize the egoi toolkit with optional credentials.

        Args:
            credentials: EgoiCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all egoi tools with the configured credentials."""
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
        """Get all egoi tools with default credentials."""
        return get_egoi_tools()
