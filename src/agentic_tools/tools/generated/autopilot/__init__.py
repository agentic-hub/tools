# autopilot toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_autopilot_tools() -> List[BaseTool]:
    """Get all autopilot tools."""
    from . import operations
    return operations.get_tools()

class AutopilotCredentials(BaseModel):
    """Credentials for autopilot authentication."""
    autopilot_api: Optional[Dict[str, Any]] = Field(None, description="autopilotApi")

class AutopilotToolkit(AgenticHubToolkit):
    """Toolkit for interacting with autopilot."""

    def __init__(self, credentials: Optional[AutopilotCredentials] = None):
        """Initialize the autopilot toolkit with optional credentials.

        Args:
            credentials: AutopilotCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all autopilot tools with the configured credentials."""
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
        """Get all autopilot tools with default credentials."""
        return get_autopilot_tools()
