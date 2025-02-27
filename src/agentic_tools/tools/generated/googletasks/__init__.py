# googletasks toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googletasks_tools() -> List[BaseTool]:
    """Get all googletasks tools."""
    from . import operations
    return operations.get_tools()

class GoogletasksCredentials(BaseModel):
    """Credentials for googletasks authentication."""
    google_tasks_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleTasksOAuth2Api")

class GoogletasksToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googletasks."""

    def __init__(self, credentials: Optional[GoogletasksCredentials] = None):
        """Initialize the googletasks toolkit with optional credentials.

        Args:
            credentials: GoogletasksCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googletasks tools with the configured credentials."""
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
        """Get all googletasks tools with default credentials."""
        return get_googletasks_tools()
