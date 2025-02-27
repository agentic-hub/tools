# venafitlsprotectcloud toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_venafitlsprotectcloud_tools() -> List[BaseTool]:
    """Get all venafitlsprotectcloud tools."""
    from . import operations
    return operations.get_tools()

class VenafitlsprotectcloudCredentials(BaseModel):
    """Credentials for venafitlsprotectcloud authentication."""
    venafi_tls_protect_cloud_api: Optional[Dict[str, Any]] = Field(None, description="venafiTlsProtectCloudApi")

class VenafitlsprotectcloudToolkit(AgenticHubToolkit):
    """Toolkit for interacting with venafitlsprotectcloud."""

    def __init__(self, credentials: Optional[VenafitlsprotectcloudCredentials] = None):
        """Initialize the venafitlsprotectcloud toolkit with optional credentials.

        Args:
            credentials: VenafitlsprotectcloudCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all venafitlsprotectcloud tools with the configured credentials."""
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
        """Get all venafitlsprotectcloud tools with default credentials."""
        return get_venafitlsprotectcloud_tools()
