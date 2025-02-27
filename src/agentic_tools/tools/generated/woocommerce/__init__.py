# woocommerce toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_woocommerce_tools() -> List[BaseTool]:
    """Get all woocommerce tools."""
    from . import operations
    return operations.get_tools()

class WoocommerceCredentials(BaseModel):
    """Credentials for woocommerce authentication."""
    woo_commerce_api: Optional[Dict[str, Any]] = Field(None, description="wooCommerceApi")

class WoocommerceToolkit(AgenticHubToolkit):
    """Toolkit for interacting with woocommerce."""

    def __init__(self, credentials: Optional[WoocommerceCredentials] = None):
        """Initialize the woocommerce toolkit with optional credentials.

        Args:
            credentials: WoocommerceCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all woocommerce tools with the configured credentials."""
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
        """Get all woocommerce tools with default credentials."""
        return get_woocommerce_tools()
