# scade-tools toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_scade-tools_tools() -> List[BaseTool]:
    """Get all scade-tools tools."""
    from . import operations
    return operations.get_tools()

class Scade-toolsCredentials(BaseModel):
    """Credentials for scade-tools authentication."""
    n8n_api: Optional[Dict[str, Any]] = Field(None, description="n8nApi")

class ScadeToolsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with scade-tools."""

    def __init__(self, credentials: Optional[Scade-toolsCredentials] = None):
        """Initialize the scade-tools toolkit with optional credentials.

        Args:
            credentials: Scade-toolsCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all scade-tools tools with the configured credentials."""
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
        """Get all scade-tools tools with default credentials."""
        return get_scade-tools_tools()
