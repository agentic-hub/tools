# rundeck toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_rundeck_tools() -> List[BaseTool]:
    """Get all rundeck tools."""
    from . import operations
    return operations.get_tools()

class RundeckCredentials(BaseModel):
    """Credentials for rundeck authentication."""
    rundeck_api: Optional[Dict[str, Any]] = Field(None, description="rundeckApi")

class RundeckToolkit(AgenticHubToolkit):
    """Toolkit for interacting with rundeck."""

    def __init__(self, credentials: Optional[RundeckCredentials] = None):
        """Initialize the rundeck toolkit with optional credentials.

        Args:
            credentials: RundeckCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all rundeck tools with the configured credentials."""
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
        """Get all rundeck tools with default credentials."""
        return get_rundeck_tools()
