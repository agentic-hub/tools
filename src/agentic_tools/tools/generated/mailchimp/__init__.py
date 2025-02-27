# mailchimp toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mailchimp_tools() -> List[BaseTool]:
    """Get all mailchimp tools."""
    from . import operations
    return operations.get_tools()

class MailchimpCredentials(BaseModel):
    """Credentials for mailchimp authentication."""
    mailchimp_api: Optional[Dict[str, Any]] = Field(None, description="mailchimpApi")
    mailchimp_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="mailchimpOAuth2Api")

class MailchimpToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mailchimp."""

    def __init__(self, credentials: Optional[MailchimpCredentials] = None):
        """Initialize the mailchimp toolkit with optional credentials.

        Args:
            credentials: MailchimpCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mailchimp tools with the configured credentials."""
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
        """Get all mailchimp tools with default credentials."""
        return get_mailchimp_tools()
