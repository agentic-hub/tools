# magento2 toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_magento2_tools() -> List[BaseTool]:
    """Get all magento2 tools."""
    from . import operations
    return operations.get_tools()

class Magento2Credentials(BaseModel):
    """Credentials for magento2 authentication."""
    magento2_api: Optional[Dict[str, Any]] = Field(None, description="magento2Api")

class MagentoToolkit(AgenticHubToolkit):
    """Toolkit for interacting with magento2."""

    def __init__(self, credentials: Optional[Magento2Credentials] = None):
        """Initialize the magento2 toolkit with optional credentials.

        Args:
            credentials: Magento2Credentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all magento2 tools with the configured credentials."""
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
        """Get all magento2 tools with default credentials."""
        return get_magento2_tools()
