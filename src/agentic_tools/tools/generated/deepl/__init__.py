# deepl toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_deepl_tools() -> List[BaseTool]:
    """Get all deepl tools."""
    from . import operations
    return operations.get_tools()

class DeeplCredentials(BaseModel):
    """Credentials for deepl authentication."""
    deep_l_api: Optional[Dict[str, Any]] = Field(None, description="deepLApi")

class DeeplToolkit(AgenticHubToolkit):
    """Toolkit for interacting with deepl."""

    def __init__(self, credentials: Optional[DeeplCredentials] = None):
        """Initialize the deepl toolkit with optional credentials.

        Args:
            credentials: DeeplCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all deepl tools with the configured credentials."""
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
        """Get all deepl tools with default credentials."""
        return get_deepl_tools()
