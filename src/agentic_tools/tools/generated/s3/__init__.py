# s3 toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_s3_tools() -> List[BaseTool]:
    """Get all s3 tools."""
    from . import operations
    return operations.get_tools()

class S3Credentials(BaseModel):
    """Credentials for s3 authentication."""
    s3: Optional[Dict[str, Any]] = Field(None, description="s3")

class SToolkit(AgenticHubToolkit):
    """Toolkit for interacting with s3."""

    def __init__(self, credentials: Optional[S3Credentials] = None):
        """Initialize the s3 toolkit with optional credentials.

        Args:
            credentials: S3Credentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all s3 tools with the configured credentials."""
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
        """Get all s3 tools with default credentials."""
        return get_s3_tools()
