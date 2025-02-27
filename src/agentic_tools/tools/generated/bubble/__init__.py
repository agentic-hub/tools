# bubble toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_bubble_tools() -> List[BaseTool]:
    """Get all bubble tools."""
    from . import operations
    return operations.get_tools()

class BubbleCredentials(BaseModel):
    """Credentials for bubble authentication."""
    bubble_api: Optional[Dict[str, Any]] = Field(None, description="bubbleApi")

class BubbleToolkit(AgenticHubToolkit):
    """Toolkit for interacting with bubble."""

    def __init__(self, credentials: Optional[BubbleCredentials] = None):
        """Initialize the bubble toolkit with optional credentials.

        Args:
            credentials: BubbleCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all bubble tools with the configured credentials."""
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
        """Get all bubble tools with default credentials."""
        return get_bubble_tools()
