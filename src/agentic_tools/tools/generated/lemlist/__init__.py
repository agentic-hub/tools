# lemlist toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_lemlist_tools() -> List[BaseTool]:
    """Get all lemlist tools."""
    from . import operations
    return operations.get_tools()

class LemlistCredentials(BaseModel):
    """Credentials for lemlist authentication."""
    lemlist_api: Optional[Dict[str, Any]] = Field(None, description="lemlistApi")

class LemlistToolkit(AgenticHubToolkit):
    """Toolkit for interacting with lemlist."""

    def __init__(self, credentials: Optional[LemlistCredentials] = None):
        """Initialize the lemlist toolkit with optional credentials.

        Args:
            credentials: LemlistCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all lemlist tools with the configured credentials."""
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
        """Get all lemlist tools with default credentials."""
        return get_lemlist_tools()
