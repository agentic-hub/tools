# phantombuster toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_phantombuster_tools() -> List[BaseTool]:
    """Get all phantombuster tools."""
    from . import operations
    return operations.get_tools()

class PhantombusterCredentials(BaseModel):
    """Credentials for phantombuster authentication."""
    phantombuster_api: Optional[Dict[str, Any]] = Field(None, description="phantombusterApi")

class PhantombusterToolkit(AgenticHubToolkit):
    """Toolkit for interacting with phantombuster."""

    def __init__(self, credentials: Optional[PhantombusterCredentials] = None):
        """Initialize the phantombuster toolkit with optional credentials.

        Args:
            credentials: PhantombusterCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all phantombuster tools with the configured credentials."""
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
        """Get all phantombuster tools with default credentials."""
        return get_phantombuster_tools()
