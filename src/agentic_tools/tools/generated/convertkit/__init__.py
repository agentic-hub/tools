# convertkit toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_convertkit_tools() -> List[BaseTool]:
    """Get all convertkit tools."""
    from . import operations
    return operations.get_tools()

class ConvertkitCredentials(BaseModel):
    """Credentials for convertkit authentication."""
    convert_kit_api: Optional[Dict[str, Any]] = Field(None, description="convertKitApi")

class ConvertkitToolkit(AgenticHubToolkit):
    """Toolkit for interacting with convertkit."""

    def __init__(self, credentials: Optional[ConvertkitCredentials] = None):
        """Initialize the convertkit toolkit with optional credentials.

        Args:
            credentials: ConvertkitCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all convertkit tools with the configured credentials."""
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
        """Get all convertkit tools with default credentials."""
        return get_convertkit_tools()
