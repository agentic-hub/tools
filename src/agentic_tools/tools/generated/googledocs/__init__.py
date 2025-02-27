# googledocs toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googledocs_tools() -> List[BaseTool]:
    """Get all googledocs tools."""
    from . import operations
    return operations.get_tools()

class GoogledocsCredentials(BaseModel):
    """Credentials for googledocs authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    google_docs_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleDocsOAuth2Api")

class GoogledocsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googledocs."""

    def __init__(self, credentials: Optional[GoogledocsCredentials] = None):
        """Initialize the googledocs toolkit with optional credentials.

        Args:
            credentials: GoogledocsCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googledocs tools with the configured credentials."""
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
        """Get all googledocs tools with default credentials."""
        return get_googledocs_tools()
