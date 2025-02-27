# tapfiliate toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_tapfiliate_tools() -> List[BaseTool]:
    """Get all tapfiliate tools."""
    from . import operations
    return operations.get_tools()

class TapfiliateCredentials(BaseModel):
    """Credentials for tapfiliate authentication."""
    tapfiliate_api: Optional[Dict[str, Any]] = Field(None, description="tapfiliateApi")

class TapfiliateToolkit(AgenticHubToolkit):
    """Toolkit for interacting with tapfiliate."""

    def __init__(self, credentials: Optional[TapfiliateCredentials] = None):
        """Initialize the tapfiliate toolkit with optional credentials.

        Args:
            credentials: TapfiliateCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all tapfiliate tools with the configured credentials."""
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
        """Get all tapfiliate tools with default credentials."""
        return get_tapfiliate_tools()
