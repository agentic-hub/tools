# clearbit toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_clearbit_tools() -> List[BaseTool]:
    """Get all clearbit tools."""
    from . import operations
    return operations.get_tools()

class ClearbitCredentials(BaseModel):
    """Credentials for clearbit authentication."""
    clearbit_api: Optional[Dict[str, Any]] = Field(None, description="clearbitApi")

class ClearbitToolkit(AgenticHubToolkit):
    """Toolkit for interacting with clearbit."""

    def __init__(self, credentials: Optional[ClearbitCredentials] = None):
        """Initialize the clearbit toolkit with optional credentials.

        Args:
            credentials: ClearbitCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all clearbit tools with the configured credentials."""
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
        """Get all clearbit tools with default credentials."""
        return get_clearbit_tools()
