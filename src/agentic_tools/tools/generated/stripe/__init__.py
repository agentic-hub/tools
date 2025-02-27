# stripe toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_stripe_tools() -> List[BaseTool]:
    """Get all stripe tools."""
    from . import operations
    return operations.get_tools()

class StripeCredentials(BaseModel):
    """Credentials for stripe authentication."""
    stripe_api: Optional[Dict[str, Any]] = Field(None, description="stripeApi")

class StripeToolkit(AgenticHubToolkit):
    """Toolkit for interacting with stripe."""

    def __init__(self, credentials: Optional[StripeCredentials] = None):
        """Initialize the stripe toolkit with optional credentials.

        Args:
            credentials: StripeCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all stripe tools with the configured credentials."""
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
        """Get all stripe tools with default credentials."""
        return get_stripe_tools()
