# mailerlite toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mailerlite_tools() -> List[BaseTool]:
    """Get all mailerlite tools."""
    from . import operations
    return operations.get_tools()

class MailerliteCredentials(BaseModel):
    """Credentials for mailerlite authentication."""
    mailer_lite_api: Optional[Dict[str, Any]] = Field(None, description="mailerLiteApi")

class MailerliteToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mailerlite."""

    def __init__(self, credentials: Optional[MailerliteCredentials] = None):
        """Initialize the mailerlite toolkit with optional credentials.

        Args:
            credentials: MailerliteCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mailerlite tools with the configured credentials."""
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
        """Get all mailerlite tools with default credentials."""
        return get_mailerlite_tools()
