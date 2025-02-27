# affinity toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_affinity_tools() -> List[BaseTool]:
    """Get all affinity tools."""
    from . import operations
    return operations.get_tools()

class AffinityCredentials(BaseModel):
    """Credentials for affinity authentication."""
    affinity_api: Optional[Dict[str, Any]] = Field(None, description="affinityApi")

class AffinityToolkit(AgenticHubToolkit):
    """Toolkit for interacting with affinity."""

    def __init__(self, credentials: Optional[AffinityCredentials] = None):
        """Initialize the affinity toolkit with optional credentials.

        Args:
            credentials: AffinityCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all affinity tools with the configured credentials."""
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
        """Get all affinity tools with default credentials."""
        return get_affinity_tools()
