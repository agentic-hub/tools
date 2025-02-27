# mailcheck toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mailcheck_tools() -> List[BaseTool]:
    """Get all mailcheck tools."""
    from . import operations
    return operations.get_tools()

class MailcheckCredentials(BaseModel):
    """Credentials for mailcheck authentication."""
    mailcheck_api: Optional[Dict[str, Any]] = Field(None, description="mailcheckApi")

class MailcheckToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mailcheck."""

    def __init__(self, credentials: Optional[MailcheckCredentials] = None):
        """Initialize the mailcheck toolkit with optional credentials.

        Args:
            credentials: MailcheckCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mailcheck tools with the configured credentials."""
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
        """Get all mailcheck tools with default credentials."""
        return get_mailcheck_tools()
