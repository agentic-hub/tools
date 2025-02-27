# harvest toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_harvest_tools() -> List[BaseTool]:
    """Get all harvest tools."""
    from . import operations
    return operations.get_tools()

class HarvestCredentials(BaseModel):
    """Credentials for harvest authentication."""
    harvest_api: Optional[Dict[str, Any]] = Field(None, description="harvestApi")
    harvest_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="harvestOAuth2Api")

class HarvestToolkit(AgenticHubToolkit):
    """Toolkit for interacting with harvest."""

    def __init__(self, credentials: Optional[HarvestCredentials] = None):
        """Initialize the harvest toolkit with optional credentials.

        Args:
            credentials: HarvestCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all harvest tools with the configured credentials."""
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
        """Get all harvest tools with default credentials."""
        return get_harvest_tools()
