# microsoftoutlook toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_microsoftoutlook_tools() -> List[BaseTool]:
    """Get all microsoftoutlook tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftoutlookCredentials(BaseModel):
    """Credentials for microsoftoutlook authentication."""
    microsoft_outlook_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftOutlookOAuth2Api")

class MicrosoftoutlookToolkit(AgenticHubToolkit):
    """Toolkit for interacting with microsoftoutlook."""

    def __init__(self, credentials: Optional[MicrosoftoutlookCredentials] = None):
        """Initialize the microsoftoutlook toolkit with optional credentials.

        Args:
            credentials: MicrosoftoutlookCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftoutlook tools with the configured credentials."""
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
        """Get all microsoftoutlook tools with default credentials."""
        return get_microsoftoutlook_tools()
