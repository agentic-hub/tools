# googlecalendar toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_googlecalendar_tools() -> List[BaseTool]:
    """Get all googlecalendar tools."""
    from . import operations
    return operations.get_tools()

class GooglecalendarCredentials(BaseModel):
    """Credentials for googlecalendar authentication."""
    google_calendar_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="googleCalendarOAuth2Api")

class GooglecalendarToolkit(AgenticHubToolkit):
    """Toolkit for interacting with googlecalendar."""

    def __init__(self, credentials: Optional[GooglecalendarCredentials] = None):
        """Initialize the googlecalendar toolkit with optional credentials.

        Args:
            credentials: GooglecalendarCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all googlecalendar tools with the configured credentials."""
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
        """Get all googlecalendar tools with default credentials."""
        return get_googlecalendar_tools()
