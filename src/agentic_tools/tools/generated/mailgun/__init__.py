# mailgun toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mailgun_tools() -> List[BaseTool]:
    """Get all mailgun tools."""
    from . import operations
    return operations.get_tools()

class MailgunCredentials(BaseModel):
    """Credentials for mailgun authentication."""
    mailgun_api: Optional[Dict[str, Any]] = Field(None, description="mailgunApi")

class MailgunToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mailgun."""

    def __init__(self, credentials: Optional[MailgunCredentials] = None):
        """Initialize the mailgun toolkit with optional credentials.

        Args:
            credentials: MailgunCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mailgun tools with the configured credentials."""
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
        """Get all mailgun tools with default credentials."""
        return get_mailgun_tools()
