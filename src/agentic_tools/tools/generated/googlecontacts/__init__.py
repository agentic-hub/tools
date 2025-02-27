# googlecontacts toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googlecontacts_tools() -> List[BaseTool]:
    """Get all googlecontacts tools."""
    from . import operations
    return operations.get_tools()

class GooglecontactsCredentials(BaseModel):
    """Credentials for googlecontacts authentication."""
    google_contacts_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleContactsOAuth2Api")

class GooglecontactsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googlecontacts."""

    def __init__(self, credentials: Optional[GooglecontactsCredentials] = None):
        """Initialize the googlecontacts toolkit with optional credentials.

        Args:
            credentials: GooglecontactsCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googlecontacts tools with the configured credentials."""
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
        """Get all googlecontacts tools with default credentials."""
        return get_googlecontacts_tools()
