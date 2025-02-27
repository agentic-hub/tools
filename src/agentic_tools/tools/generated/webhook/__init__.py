# webhook toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_webhook_tools() -> List[BaseTool]:
    """Get all webhook tools."""
    from . import operations
    return operations.get_tools()

class WebhookCredentials(BaseModel):
    """Credentials for webhook authentication."""
    http_basic_auth: Optional[Dict[str, Any]] = Field(None, description="httpBasicAuth")
    http_header_auth: Optional[Dict[str, Any]] = Field(None, description="httpHeaderAuth")

class WebhookToolkit(AgenticHubToolkit):
    """Toolkit for interacting with webhook."""

    def __init__(self, credentials: Optional[WebhookCredentials] = None):
        """Initialize the webhook toolkit with optional credentials.

        Args:
            credentials: WebhookCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all webhook tools with the configured credentials."""
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
        """Get all webhook tools with default credentials."""
        return get_webhook_tools()
