# customerio toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_customerio_tools() -> List[BaseTool]:
    """Get all customerio tools."""
    from . import operations
    return operations.get_tools()

class CustomerioCredentials(BaseModel):
    """Credentials for customerio authentication."""
    customer_io_api: Optional[Dict[str, Any]] = Field(None, description="customerIoApi")

class CustomerioToolkit(AgenticHubToolkit):
    """Toolkit for interacting with customerio."""

    def __init__(self, credentials: Optional[CustomerioCredentials] = None):
        """Initialize the customerio toolkit with optional credentials.

        Args:
            credentials: CustomerioCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all customerio tools with the configured credentials."""
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
        """Get all customerio tools with default credentials."""
        return get_customerio_tools()
