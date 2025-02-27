# unleashedsoftware toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_unleashedsoftware_tools() -> List[BaseTool]:
    """Get all unleashedsoftware tools."""
    from . import operations
    return operations.get_tools()

class UnleashedsoftwareCredentials(BaseModel):
    """Credentials for unleashedsoftware authentication."""
    unleashed_software_api: Optional[Dict[str, Any]] = Field(None, description="unleashedSoftwareApi")

class UnleashedsoftwareToolkit(AgenticHubToolkit):
    """Toolkit for interacting with unleashedsoftware."""

    def __init__(self, credentials: Optional[UnleashedsoftwareCredentials] = None):
        """Initialize the unleashedsoftware toolkit with optional credentials.

        Args:
            credentials: UnleashedsoftwareCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all unleashedsoftware tools with the configured credentials."""
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
        """Get all unleashedsoftware tools with default credentials."""
        return get_unleashedsoftware_tools()
