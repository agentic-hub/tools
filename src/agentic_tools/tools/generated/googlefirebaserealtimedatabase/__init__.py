# googlefirebaserealtimedatabase toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googlefirebaserealtimedatabase_tools() -> List[BaseTool]:
    """Get all googlefirebaserealtimedatabase tools."""
    from . import operations
    return operations.get_tools()

class GooglefirebaserealtimedatabaseCredentials(BaseModel):
    """Credentials for googlefirebaserealtimedatabase authentication."""
    google_firebase_realtime_database_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleFirebaseRealtimeDatabaseOAuth2Api")

class GooglefirebaserealtimedatabaseToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googlefirebaserealtimedatabase."""

    def __init__(self, credentials: Optional[GooglefirebaserealtimedatabaseCredentials] = None):
        """Initialize the googlefirebaserealtimedatabase toolkit with optional credentials.

        Args:
            credentials: GooglefirebaserealtimedatabaseCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googlefirebaserealtimedatabase tools with the configured credentials."""
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
        """Get all googlefirebaserealtimedatabase tools with default credentials."""
        return get_googlefirebaserealtimedatabase_tools()
