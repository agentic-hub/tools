# googlecloudstorage toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googlecloudstorage_tools() -> List[BaseTool]:
    """Get all googlecloudstorage tools."""
    from . import operations
    return operations.get_tools()

class GooglecloudstorageCredentials(BaseModel):
    """Credentials for googlecloudstorage authentication."""
    google_cloud_storage_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleCloudStorageOAuth2Api")

class GooglecloudstorageToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googlecloudstorage."""

    def __init__(self, credentials: Optional[GooglecloudstorageCredentials] = None):
        """Initialize the googlecloudstorage toolkit with optional credentials.

        Args:
            credentials: GooglecloudstorageCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googlecloudstorage tools with the configured credentials."""
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
        """Get all googlecloudstorage tools with default credentials."""
        return get_googlecloudstorage_tools()
