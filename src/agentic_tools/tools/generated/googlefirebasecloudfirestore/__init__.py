# googlefirebasecloudfirestore toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googlefirebasecloudfirestore_tools() -> List[BaseTool]:
    """Get all googlefirebasecloudfirestore tools."""
    from . import operations
    return operations.get_tools()

class GooglefirebasecloudfirestoreCredentials(BaseModel):
    """Credentials for googlefirebasecloudfirestore authentication."""
    google_firebase_cloud_firestore_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleFirebaseCloudFirestoreOAuth2Api")

class GooglefirebasecloudfirestoreToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googlefirebasecloudfirestore."""

    def __init__(self, credentials: Optional[GooglefirebasecloudfirestoreCredentials] = None):
        """Initialize the googlefirebasecloudfirestore toolkit with optional credentials.

        Args:
            credentials: GooglefirebasecloudfirestoreCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googlefirebasecloudfirestore tools with the configured credentials."""
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
        """Get all googlefirebasecloudfirestore tools with default credentials."""
        return get_googlefirebasecloudfirestore_tools()
