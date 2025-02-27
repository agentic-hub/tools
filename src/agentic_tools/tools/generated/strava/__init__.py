# strava toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_strava_tools() -> List[BaseTool]:
    """Get all strava tools."""
    from . import operations
    return operations.get_tools()

class StravaCredentials(BaseModel):
    """Credentials for strava authentication."""
    strava_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="stravaOAuth2Api")

class StravaToolkit(AgenticHubToolkit):
    """Toolkit for interacting with strava."""

    def __init__(self, credentials: Optional[StravaCredentials] = None):
        """Initialize the strava toolkit with optional credentials.

        Args:
            credentials: StravaCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all strava tools with the configured credentials."""
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
        """Get all strava tools with default credentials."""
        return get_strava_tools()
