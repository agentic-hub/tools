# spontit toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_spontit_tools() -> List[BaseTool]:
    """Get all spontit tools."""
    from . import operations
    return operations.get_tools()

class SpontitCredentials(BaseModel):
    """Credentials for spontit authentication."""
    spontit_api: Optional[Dict[str, Any]] = Field(None, description="spontitApi")

class SpontitToolkit(AgenticHubToolkit):
    """Toolkit for interacting with spontit."""

    def __init__(self, credentials: Optional[SpontitCredentials] = None):
        """Initialize the spontit toolkit with optional credentials.

        Args:
            credentials: SpontitCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all spontit tools with the configured credentials."""
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
        """Get all spontit tools with default credentials."""
        return get_spontit_tools()
