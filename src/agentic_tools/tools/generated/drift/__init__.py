# drift toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_drift_tools() -> List[BaseTool]:
    """Get all drift tools."""
    from . import operations
    return operations.get_tools()

class DriftCredentials(BaseModel):
    """Credentials for drift authentication."""
    drift_api: Optional[Dict[str, Any]] = Field(None, description="driftApi")
    drift_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="driftOAuth2Api")

class DriftToolkit(AgenticHubToolkit):
    """Toolkit for interacting with drift."""

    def __init__(self, credentials: Optional[DriftCredentials] = None):
        """Initialize the drift toolkit with optional credentials.

        Args:
            credentials: DriftCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all drift tools with the configured credentials."""
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
        """Get all drift tools with default credentials."""
        return get_drift_tools()
