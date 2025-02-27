# discourse toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_discourse_tools() -> List[BaseTool]:
    """Get all discourse tools."""
    from . import operations
    return operations.get_tools()

class DiscourseCredentials(BaseModel):
    """Credentials for discourse authentication."""
    discourse_api: Optional[Dict[str, Any]] = Field(None, description="discourseApi")

class DiscourseToolkit(AgenticHubToolkit):
    """Toolkit for interacting with discourse."""

    def __init__(self, credentials: Optional[DiscourseCredentials] = None):
        """Initialize the discourse toolkit with optional credentials.

        Args:
            credentials: DiscourseCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all discourse tools with the configured credentials."""
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
        """Get all discourse tools with default credentials."""
        return get_discourse_tools()
