# demio toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_demio_tools() -> List[BaseTool]:
    """Get all demio tools."""
    from . import operations
    return operations.get_tools()

class DemioCredentials(BaseModel):
    """Credentials for demio authentication."""
    demio_api: Optional[Dict[str, Any]] = Field(None, description="demioApi")

class DemioToolkit(AgenticHubToolkit):
    """Toolkit for interacting with demio."""

    def __init__(self, credentials: Optional[DemioCredentials] = None):
        """Initialize the demio toolkit with optional credentials.

        Args:
            credentials: DemioCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all demio tools with the configured credentials."""
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
        """Get all demio tools with default credentials."""
        return get_demio_tools()
