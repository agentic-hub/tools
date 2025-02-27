# orbit toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_orbit_tools() -> List[BaseTool]:
    """Get all orbit tools."""
    from . import operations
    return operations.get_tools()

class OrbitCredentials(BaseModel):
    """Credentials for orbit authentication."""
    orbit_api: Optional[Dict[str, Any]] = Field(None, description="orbitApi")

class OrbitToolkit(AgenticHubToolkit):
    """Toolkit for interacting with orbit."""

    def __init__(self, credentials: Optional[OrbitCredentials] = None):
        """Initialize the orbit toolkit with optional credentials.

        Args:
            credentials: OrbitCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all orbit tools with the configured credentials."""
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
        """Get all orbit tools with default credentials."""
        return get_orbit_tools()
