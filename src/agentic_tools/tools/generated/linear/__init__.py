# linear toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_linear_tools() -> List[BaseTool]:
    """Get all linear tools."""
    from . import operations
    return operations.get_tools()

class LinearCredentials(BaseModel):
    """Credentials for linear authentication."""
    linear_api: Optional[Dict[str, Any]] = Field(None, description="linearApi")
    linear_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="linearOAuth2Api")

class LinearToolkit(AgenticHubToolkit):
    """Toolkit for interacting with linear."""

    def __init__(self, credentials: Optional[LinearCredentials] = None):
        """Initialize the linear toolkit with optional credentials.

        Args:
            credentials: LinearCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all linear tools with the configured credentials."""
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
        """Get all linear tools with default credentials."""
        return get_linear_tools()
