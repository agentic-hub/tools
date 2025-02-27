# disqus toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_disqus_tools() -> List[BaseTool]:
    """Get all disqus tools."""
    from . import operations
    return operations.get_tools()

class DisqusCredentials(BaseModel):
    """Credentials for disqus authentication."""
    disqus_api: Optional[Dict[str, Any]] = Field(None, description="disqusApi")

class DisqusToolkit(AgenticHubToolkit):
    """Toolkit for interacting with disqus."""

    def __init__(self, credentials: Optional[DisqusCredentials] = None):
        """Initialize the disqus toolkit with optional credentials.

        Args:
            credentials: DisqusCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all disqus tools with the configured credentials."""
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
        """Get all disqus tools with default credentials."""
        return get_disqus_tools()
