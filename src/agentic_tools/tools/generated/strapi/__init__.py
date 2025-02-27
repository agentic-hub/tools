# strapi toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_strapi_tools() -> List[BaseTool]:
    """Get all strapi tools."""
    from . import operations
    return operations.get_tools()

class StrapiCredentials(BaseModel):
    """Credentials for strapi authentication."""
    strapi_api: Optional[Dict[str, Any]] = Field(None, description="strapiApi")
    strapi_token_api: Optional[Dict[str, Any]] = Field(None, description="strapiTokenApi")

class StrapiToolkit(AgenticHubToolkit):
    """Toolkit for interacting with strapi."""

    def __init__(self, credentials: Optional[StrapiCredentials] = None):
        """Initialize the strapi toolkit with optional credentials.

        Args:
            credentials: StrapiCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all strapi tools with the configured credentials."""
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
        """Get all strapi tools with default credentials."""
        return get_strapi_tools()
