# crowddev toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_crowddev_tools() -> List[BaseTool]:
    """Get all crowddev tools."""
    from . import operations
    return operations.get_tools()

class CrowddevCredentials(BaseModel):
    """Credentials for crowddev authentication."""
    crowd_dev_api: Optional[Dict[str, Any]] = Field(None, description="crowdDevApi")

class CrowddevToolkit(AgenticHubToolkit):
    """Toolkit for interacting with crowddev."""

    def __init__(self, credentials: Optional[CrowddevCredentials] = None):
        """Initialize the crowddev toolkit with optional credentials.

        Args:
            credentials: CrowddevCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all crowddev tools with the configured credentials."""
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
        """Get all crowddev tools with default credentials."""
        return get_crowddev_tools()
