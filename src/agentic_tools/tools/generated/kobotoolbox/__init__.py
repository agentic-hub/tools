# kobotoolbox toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_kobotoolbox_tools() -> List[BaseTool]:
    """Get all kobotoolbox tools."""
    from . import operations
    return operations.get_tools()

class KobotoolboxCredentials(BaseModel):
    """Credentials for kobotoolbox authentication."""
    ko_bo_toolbox_api: Optional[Dict[str, Any]] = Field(None, description="koBoToolboxApi")

class KobotoolboxToolkit(AgenticHubToolkit):
    """Toolkit for interacting with kobotoolbox."""

    def __init__(self, credentials: Optional[KobotoolboxCredentials] = None):
        """Initialize the kobotoolbox toolkit with optional credentials.

        Args:
            credentials: KobotoolboxCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all kobotoolbox tools with the configured credentials."""
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
        """Get all kobotoolbox tools with default credentials."""
        return get_kobotoolbox_tools()
