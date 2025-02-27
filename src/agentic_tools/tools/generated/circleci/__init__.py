# circleci toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_circleci_tools() -> List[BaseTool]:
    """Get all circleci tools."""
    from . import operations
    return operations.get_tools()

class CircleciCredentials(BaseModel):
    """Credentials for circleci authentication."""
    circle_ci_api: Optional[Dict[str, Any]] = Field(None, description="circleCiApi")

class CircleciToolkit(AgenticHubToolkit):
    """Toolkit for interacting with circleci."""

    def __init__(self, credentials: Optional[CircleciCredentials] = None):
        """Initialize the circleci toolkit with optional credentials.

        Args:
            credentials: CircleciCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all circleci tools with the configured credentials."""
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
        """Get all circleci tools with default credentials."""
        return get_circleci_tools()
