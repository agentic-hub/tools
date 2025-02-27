# seatable toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_seatable_tools() -> List[BaseTool]:
    """Get all seatable tools."""
    from . import operations
    return operations.get_tools()

class SeatableCredentials(BaseModel):
    """Credentials for seatable authentication."""
    sea_table_api: Optional[Dict[str, Any]] = Field(None, description="seaTableApi")

class SeatableToolkit(AgenticHubToolkit):
    """Toolkit for interacting with seatable."""

    def __init__(self, credentials: Optional[SeatableCredentials] = None):
        """Initialize the seatable toolkit with optional credentials.

        Args:
            credentials: SeatableCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all seatable tools with the configured credentials."""
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
        """Get all seatable tools with default credentials."""
        return get_seatable_tools()
