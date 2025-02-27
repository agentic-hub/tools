# awstranscribe toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_awstranscribe_tools() -> List[BaseTool]:
    """Get all awstranscribe tools."""
    from . import operations
    return operations.get_tools()

class AwstranscribeCredentials(BaseModel):
    """Credentials for awstranscribe authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwsTranscribeToolkit(AgenticHubToolkit):
    """Toolkit for interacting with awstranscribe."""

    def __init__(self, credentials: Optional[AwstranscribeCredentials] = None):
        """Initialize the awstranscribe toolkit with optional credentials.

        Args:
            credentials: AwstranscribeCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all awstranscribe tools with the configured credentials."""
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
        """Get all awstranscribe tools with default credentials."""
        return get_awstranscribe_tools()
