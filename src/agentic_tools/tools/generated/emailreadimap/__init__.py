# emailreadimap toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_emailreadimap_tools() -> List[BaseTool]:
    """Get all emailreadimap tools."""
    from . import operations
    return operations.get_tools()

class EmailreadimapCredentials(BaseModel):
    """Credentials for emailreadimap authentication."""
    imap: Optional[Dict[str, Any]] = Field(None, description="imap")

class EmailreadimapToolkit(AgenticHubToolkit):
    """Toolkit for interacting with emailreadimap."""

    def __init__(self, credentials: Optional[EmailreadimapCredentials] = None):
        """Initialize the emailreadimap toolkit with optional credentials.

        Args:
            credentials: EmailreadimapCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all emailreadimap tools with the configured credentials."""
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
        """Get all emailreadimap tools with default credentials."""
        return get_emailreadimap_tools()
