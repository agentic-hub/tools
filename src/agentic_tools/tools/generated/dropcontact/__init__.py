# dropcontact toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_dropcontact_tools() -> List[BaseTool]:
    """Get all dropcontact tools."""
    from . import operations
    return operations.get_tools()

class DropcontactCredentials(BaseModel):
    """Credentials for dropcontact authentication."""
    dropcontact_api: Optional[Dict[str, Any]] = Field(None, description="dropcontactApi")

class DropcontactToolkit(AgenticHubToolkit):
    """Toolkit for interacting with dropcontact."""

    def __init__(self, credentials: Optional[DropcontactCredentials] = None):
        """Initialize the dropcontact toolkit with optional credentials.

        Args:
            credentials: DropcontactCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all dropcontact tools with the configured credentials."""
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
        """Get all dropcontact tools with default credentials."""
        return get_dropcontact_tools()
