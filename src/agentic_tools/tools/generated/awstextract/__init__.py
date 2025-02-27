# awstextract toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_awstextract_tools() -> List[BaseTool]:
    """Get all awstextract tools."""
    from . import operations
    return operations.get_tools()

class AwstextractCredentials(BaseModel):
    """Credentials for awstextract authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwsTextractToolkit(AgenticHubToolkit):
    """Toolkit for interacting with awstextract."""

    def __init__(self, credentials: Optional[AwstextractCredentials] = None):
        """Initialize the awstextract toolkit with optional credentials.

        Args:
            credentials: AwstextractCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all awstextract tools with the configured credentials."""
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
        """Get all awstextract tools with default credentials."""
        return get_awstextract_tools()
