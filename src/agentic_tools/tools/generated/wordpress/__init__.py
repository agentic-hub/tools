# wordpress toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_wordpress_tools() -> List[BaseTool]:
    """Get all wordpress tools."""
    from . import operations
    return operations.get_tools()

class WordpressCredentials(BaseModel):
    """Credentials for wordpress authentication."""
    wordpress_api: Optional[Dict[str, Any]] = Field(None, description="wordpressApi")

class WordpressToolkit(AgenticHubToolkit):
    """Toolkit for interacting with wordpress."""

    def __init__(self, credentials: Optional[WordpressCredentials] = None):
        """Initialize the wordpress toolkit with optional credentials.

        Args:
            credentials: WordpressCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all wordpress tools with the configured credentials."""
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
        """Get all wordpress tools with default credentials."""
        return get_wordpress_tools()
