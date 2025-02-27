# nextcloud toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_nextcloud_tools() -> List[BaseTool]:
    """Get all nextcloud tools."""
    from . import operations
    return operations.get_tools()

class NextcloudCredentials(BaseModel):
    """Credentials for nextcloud authentication."""
    next_cloud_api: Optional[Dict[str, Any]] = Field(None, description="nextCloudApi")
    next_cloud_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="nextCloudOAuth2Api")

class NextcloudToolkit(AgenticHubToolkit):
    """Toolkit for interacting with nextcloud."""

    def __init__(self, credentials: Optional[NextcloudCredentials] = None):
        """Initialize the nextcloud toolkit with optional credentials.

        Args:
            credentials: NextcloudCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all nextcloud tools with the configured credentials."""
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
        """Get all nextcloud tools with default credentials."""
        return get_nextcloud_tools()
