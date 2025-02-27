# emelia toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_emelia_tools() -> List[BaseTool]:
    """Get all emelia tools."""
    from . import operations
    return operations.get_tools()

class EmeliaCredentials(BaseModel):
    """Credentials for emelia authentication."""
    emelia_api: Optional[Dict[str, Any]] = Field(None, description="emeliaApi")

class EmeliaToolkit(AgenticHubToolkit):
    """Toolkit for interacting with emelia."""

    def __init__(self, credentials: Optional[EmeliaCredentials] = None):
        """Initialize the emelia toolkit with optional credentials.

        Args:
            credentials: EmeliaCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all emelia tools with the configured credentials."""
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
        """Get all emelia tools with default credentials."""
        return get_emelia_tools()
