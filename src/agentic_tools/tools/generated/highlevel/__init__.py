# highlevel toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_highlevel_tools() -> List[BaseTool]:
    """Get all highlevel tools."""
    from . import operations
    return operations.get_tools()

class HighlevelCredentials(BaseModel):
    """Credentials for highlevel authentication."""
    high_level_api: Optional[Dict[str, Any]] = Field(None, description="highLevelApi")

class HighlevelToolkit(AgenticHubToolkit):
    """Toolkit for interacting with highlevel."""

    def __init__(self, credentials: Optional[HighlevelCredentials] = None):
        """Initialize the highlevel toolkit with optional credentials.

        Args:
            credentials: HighlevelCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all highlevel tools with the configured credentials."""
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
        """Get all highlevel tools with default credentials."""
        return get_highlevel_tools()
