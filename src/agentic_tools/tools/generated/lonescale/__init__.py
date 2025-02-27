# lonescale toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_lonescale_tools() -> List[BaseTool]:
    """Get all lonescale tools."""
    from . import operations
    return operations.get_tools()

class LonescaleCredentials(BaseModel):
    """Credentials for lonescale authentication."""
    lone_scale_api: Optional[Dict[str, Any]] = Field(None, description="loneScaleApi")

class LonescaleToolkit(AgenticHubToolkit):
    """Toolkit for interacting with lonescale."""

    def __init__(self, credentials: Optional[LonescaleCredentials] = None):
        """Initialize the lonescale toolkit with optional credentials.

        Args:
            credentials: LonescaleCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all lonescale tools with the configured credentials."""
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
        """Get all lonescale tools with default credentials."""
        return get_lonescale_tools()
