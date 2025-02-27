# googlesheets toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googlesheets_tools() -> List[BaseTool]:
    """Get all googlesheets tools."""
    from . import operations
    return operations.get_tools()

class GooglesheetsCredentials(BaseModel):
    """Credentials for googlesheets authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_sheets_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleSheetsOAuth2Api")

class GooglesheetsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googlesheets."""

    def __init__(self, credentials: Optional[GooglesheetsCredentials] = None):
        """Initialize the googlesheets toolkit with optional credentials.

        Args:
            credentials: GooglesheetsCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googlesheets tools with the configured credentials."""
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
        """Get all googlesheets tools with default credentials."""
        return get_googlesheets_tools()
