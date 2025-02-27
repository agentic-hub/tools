# mailjet toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mailjet_tools() -> List[BaseTool]:
    """Get all mailjet tools."""
    from . import operations
    return operations.get_tools()

class MailjetCredentials(BaseModel):
    """Credentials for mailjet authentication."""
    mailjet_email_api: Optional[Dict[str, Any]] = Field(None, description="mailjetEmailApi")
    mailjet_sms_api: Optional[Dict[str, Any]] = Field(None, description="mailjetSmsApi")

class MailjetToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mailjet."""

    def __init__(self, credentials: Optional[MailjetCredentials] = None):
        """Initialize the mailjet toolkit with optional credentials.

        Args:
            credentials: MailjetCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mailjet tools with the configured credentials."""
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
        """Get all mailjet tools with default credentials."""
        return get_mailjet_tools()
