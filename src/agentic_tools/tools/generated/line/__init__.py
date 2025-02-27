# line toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_line_tools() -> List[BaseTool]:
    """Get all line tools."""
    from . import operations
    return operations.get_tools()

class LineCredentials(BaseModel):
    """Credentials for line authentication."""
    line_notify_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="lineNotifyOAuth2Api")

class LineToolkit(AgenticHubToolkit):
    """Toolkit for interacting with line."""

    def __init__(self, credentials: Optional[LineCredentials] = None):
        """Initialize the line toolkit with optional credentials.

        Args:
            credentials: LineCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all line tools with the configured credentials."""
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
        """Get all line tools with default credentials."""
        return get_line_tools()
