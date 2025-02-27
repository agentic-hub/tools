# googlecloudnaturallanguage toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googlecloudnaturallanguage_tools() -> List[BaseTool]:
    """Get all googlecloudnaturallanguage tools."""
    from . import operations
    return operations.get_tools()

class GooglecloudnaturallanguageCredentials(BaseModel):
    """Credentials for googlecloudnaturallanguage authentication."""
    google_cloud_natural_language_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleCloudNaturalLanguageOAuth2Api")

class GooglecloudnaturallanguageToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googlecloudnaturallanguage."""

    def __init__(self, credentials: Optional[GooglecloudnaturallanguageCredentials] = None):
        """Initialize the googlecloudnaturallanguage toolkit with optional credentials.

        Args:
            credentials: GooglecloudnaturallanguageCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googlecloudnaturallanguage tools with the configured credentials."""
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
        """Get all googlecloudnaturallanguage tools with default credentials."""
        return get_googlecloudnaturallanguage_tools()
