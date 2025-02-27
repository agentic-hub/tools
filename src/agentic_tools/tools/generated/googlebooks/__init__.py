# googlebooks toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googlebooks_tools() -> List[BaseTool]:
    """Get all googlebooks tools."""
    from . import operations
    return operations.get_tools()

class GooglebooksCredentials(BaseModel):
    """Credentials for googlebooks authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_books_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleBooksOAuth2Api")

class GooglebooksToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googlebooks."""

    def __init__(self, credentials: Optional[GooglebooksCredentials] = None):
        """Initialize the googlebooks toolkit with optional credentials.

        Args:
            credentials: GooglebooksCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googlebooks tools with the configured credentials."""
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
        """Get all googlebooks tools with default credentials."""
        return get_googlebooks_tools()
