# shopify toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_shopify_tools() -> List[BaseTool]:
    """Get all shopify tools."""
    from . import operations
    return operations.get_tools()

class ShopifyCredentials(BaseModel):
    """Credentials for shopify authentication."""
    shopify_api: Optional[Dict[str, Any]] = Field(None, description="shopifyApi")
    shopify_access_token_api: Optional[Dict[str, Any]] = Field(None, description="shopifyAccessTokenApi")
    shopify_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="shopifyOAuth2Api")

class ShopifyToolkit(AgenticHubToolkit):
    """Toolkit for interacting with shopify."""

    def __init__(self, credentials: Optional[ShopifyCredentials] = None):
        """Initialize the shopify toolkit with optional credentials.

        Args:
            credentials: ShopifyCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all shopify tools with the configured credentials."""
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
        """Get all shopify tools with default credentials."""
        return get_shopify_tools()
