# nasa toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_nasa_tools() -> List[BaseTool]:
    """Get all nasa tools."""
    from . import operations
    return operations.get_tools()

class NasaCredentials(BaseModel):
    """Credentials for nasa authentication."""
    nasa_api: Optional[Dict[str, Any]] = Field(None, description="nasaApi")

class NasaToolkit(AgenticHubToolkit):
    """Toolkit for interacting with nasa."""

    def __init__(self, credentials: Optional[NasaCredentials] = None):
        """Initialize the nasa toolkit with optional credentials.

        Args:
            credentials: NasaCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all nasa tools with the configured credentials."""
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
        """Get all nasa tools with default credentials."""
        return get_nasa_tools()
