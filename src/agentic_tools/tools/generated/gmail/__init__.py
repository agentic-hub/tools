# gmail toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_gmail_tools() -> List[BaseTool]:
    """Get all gmail tools."""
    from . import operations
    return operations.get_tools()

class GmailCredentials(BaseModel):
    """Credentials for gmail authentication."""
    google_api: Optional[Dict[str, Any]] = Field(None, description="googleApi")
    gmail_o_auth2: Optional[Dict[str, Any]] = Field(None, description="gmailOAuth2")

class GmailToolkit(AgenticHubToolkit):
    """Toolkit for interacting with gmail."""

    def __init__(self, credentials: Optional[GmailCredentials] = None):
        """Initialize the gmail toolkit with optional credentials.

        Args:
            credentials: GmailCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all gmail tools with the configured credentials."""
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
        """Get all gmail tools with default credentials."""
        return get_gmail_tools()
