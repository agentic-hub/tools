# uptimerobot toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_uptimerobot_tools() -> List[BaseTool]:
    """Get all uptimerobot tools."""
    from . import operations
    return operations.get_tools()

class UptimerobotCredentials(BaseModel):
    """Credentials for uptimerobot authentication."""
    uptime_robot_api: Optional[Dict[str, Any]] = Field(None, description="uptimeRobotApi")

class UptimerobotToolkit(AgenticHubToolkit):
    """Toolkit for interacting with uptimerobot."""

    def __init__(self, credentials: Optional[UptimerobotCredentials] = None):
        """Initialize the uptimerobot toolkit with optional credentials.

        Args:
            credentials: UptimerobotCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all uptimerobot tools with the configured credentials."""
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
        """Get all uptimerobot tools with default credentials."""
        return get_uptimerobot_tools()
