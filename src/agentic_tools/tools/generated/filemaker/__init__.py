# filemaker toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_filemaker_tools() -> List[BaseTool]:
    """Get all filemaker tools."""
    from . import operations
    return operations.get_tools()

class FilemakerCredentials(BaseModel):
    """Credentials for filemaker authentication."""
    file_maker: Optional[Dict[str, Any]] = Field(None, description="fileMaker")

class FilemakerToolkit(AgenticHubToolkit):
    """Toolkit for interacting with filemaker."""

    def __init__(self, credentials: Optional[FilemakerCredentials] = None):
        """Initialize the filemaker toolkit with optional credentials.

        Args:
            credentials: FilemakerCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all filemaker tools with the configured credentials."""
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
        """Get all filemaker tools with default credentials."""
        return get_filemaker_tools()
