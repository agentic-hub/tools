# pushbullet toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_pushbullet_tools() -> List[BaseTool]:
    """Get all pushbullet tools."""
    from . import operations
    return operations.get_tools()

class PushbulletCredentials(BaseModel):
    """Credentials for pushbullet authentication."""
    pushbullet_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="pushbulletOAuth2Api")

class PushbulletToolkit(AgenticHubToolkit):
    """Toolkit for interacting with pushbullet."""

    def __init__(self, credentials: Optional[PushbulletCredentials] = None):
        """Initialize the pushbullet toolkit with optional credentials.

        Args:
            credentials: PushbulletCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all pushbullet tools with the configured credentials."""
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
        """Get all pushbullet tools with default credentials."""
        return get_pushbullet_tools()
