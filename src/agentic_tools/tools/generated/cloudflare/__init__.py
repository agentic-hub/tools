# cloudflare toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_cloudflare_tools() -> List[BaseTool]:
    """Get all cloudflare tools."""
    from . import operations
    return operations.get_tools()

class CloudflareCredentials(BaseModel):
    """Credentials for cloudflare authentication."""
    cloudflare_api: Optional[Dict[str, Any]] = Field(None, description="cloudflareApi")

class CloudflareToolkit(AgenticHubToolkit):
    """Toolkit for interacting with cloudflare."""

    def __init__(self, credentials: Optional[CloudflareCredentials] = None):
        """Initialize the cloudflare toolkit with optional credentials.

        Args:
            credentials: CloudflareCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all cloudflare tools with the configured credentials."""
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
        """Get all cloudflare tools with default credentials."""
        return get_cloudflare_tools()
