# thehiveproject toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_thehiveproject_tools() -> List[BaseTool]:
    """Get all thehiveproject tools."""
    from . import operations
    return operations.get_tools()

class ThehiveprojectCredentials(BaseModel):
    """Credentials for thehiveproject authentication."""
    the_hive_project_api: Optional[Dict[str, Any]] = Field(None, description="theHiveProjectApi")

class ThehiveprojectToolkit(AgenticHubToolkit):
    """Toolkit for interacting with thehiveproject."""

    def __init__(self, credentials: Optional[ThehiveprojectCredentials] = None):
        """Initialize the thehiveproject toolkit with optional credentials.

        Args:
            credentials: ThehiveprojectCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all thehiveproject tools with the configured credentials."""
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
        """Get all thehiveproject tools with default credentials."""
        return get_thehiveproject_tools()
