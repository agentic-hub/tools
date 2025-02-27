# awss3 toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_awss3_tools() -> List[BaseTool]:
    """Get all awss3 tools."""
    from . import operations
    return operations.get_tools()

class Awss3Credentials(BaseModel):
    """Credentials for awss3 authentication."""
    aws: Optional[Dict[str, Any]] = Field(None, description="aws")

class AwsS3Toolkit(AgenticHubToolkit):
    """Toolkit for interacting with awss3."""

    def __init__(self, credentials: Optional[Awss3Credentials] = None):
        """Initialize the awss3 toolkit with optional credentials.

        Args:
            credentials: Awss3Credentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all awss3 tools with the configured credentials."""
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
        """Get all awss3 tools with default credentials."""
        return get_awss3_tools()
