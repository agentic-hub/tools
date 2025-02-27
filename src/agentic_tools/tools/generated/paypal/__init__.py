# paypal toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_paypal_tools() -> List[BaseTool]:
    """Get all paypal tools."""
    from . import operations
    return operations.get_tools()

class PaypalCredentials(BaseModel):
    """Credentials for paypal authentication."""
    pay_pal_api: Optional[Dict[str, Any]] = Field(None, description="payPalApi")

class PaypalToolkit(AgenticHubToolkit):
    """Toolkit for interacting with paypal."""

    def __init__(self, credentials: Optional[PaypalCredentials] = None):
        """Initialize the paypal toolkit with optional credentials.

        Args:
            credentials: PaypalCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all paypal tools with the configured credentials."""
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
        """Get all paypal tools with default credentials."""
        return get_paypal_tools()
