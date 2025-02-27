# bamboohr toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_bamboohr_tools() -> List[BaseTool]:
    """Get all bamboohr tools."""
    from . import operations
    return operations.get_tools()

class BamboohrCredentials(BaseModel):
    """Credentials for bamboohr authentication."""
    bamboo_hr_api: Optional[Dict[str, Any]] = Field(None, description="bambooHrApi")

class BamboohrToolkit(AgenticHubToolkit):
    """Toolkit for interacting with bamboohr."""

    def __init__(self, credentials: Optional[BamboohrCredentials] = None):
        """Initialize the bamboohr toolkit with optional credentials.

        Args:
            credentials: BamboohrCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all bamboohr tools with the configured credentials."""
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
        """Get all bamboohr tools with default credentials."""
        return get_bamboohr_tools()
