# signl4 toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_signl4_tools() -> List[BaseTool]:
    """Get all signl4 tools."""
    from . import operations
    return operations.get_tools()

class Signl4Credentials(BaseModel):
    """Credentials for signl4 authentication."""
    signl4_api: Optional[Dict[str, Any]] = Field(None, description="signl4Api")

class SignlToolkit(AgenticHubToolkit):
    """Toolkit for interacting with signl4."""

    def __init__(self, credentials: Optional[Signl4Credentials] = None):
        """Initialize the signl4 toolkit with optional credentials.

        Args:
            credentials: Signl4Credentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all signl4 tools with the configured credentials."""
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
        """Get all signl4 tools with default credentials."""
        return get_signl4_tools()
