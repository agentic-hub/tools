# cortex toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_cortex_tools() -> List[BaseTool]:
    """Get all cortex tools."""
    from . import operations
    return operations.get_tools()

class CortexCredentials(BaseModel):
    """Credentials for cortex authentication."""
    cortex_api: Optional[Dict[str, Any]] = Field(None, description="cortexApi")

class CortexToolkit(AgenticHubToolkit):
    """Toolkit for interacting with cortex."""

    def __init__(self, credentials: Optional[CortexCredentials] = None):
        """Initialize the cortex toolkit with optional credentials.

        Args:
            credentials: CortexCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all cortex tools with the configured credentials."""
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
        """Get all cortex tools with default credentials."""
        return get_cortex_tools()
