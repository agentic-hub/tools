# sentryio toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_sentryio_tools() -> List[BaseTool]:
    """Get all sentryio tools."""
    from . import operations
    return operations.get_tools()

class SentryioCredentials(BaseModel):
    """Credentials for sentryio authentication."""
    sentry_io_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="sentryIoOAuth2Api")
    sentry_io_api: Optional[Dict[str, Any]] = Field(None, description="sentryIoApi")
    sentry_io_server_api: Optional[Dict[str, Any]] = Field(None, description="sentryIoServerApi")

class SentryioToolkit(AgenticHubToolkit):
    """Toolkit for interacting with sentryio."""

    def __init__(self, credentials: Optional[SentryioCredentials] = None):
        """Initialize the sentryio toolkit with optional credentials.

        Args:
            credentials: SentryioCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all sentryio tools with the configured credentials."""
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
        """Get all sentryio tools with default credentials."""
        return get_sentryio_tools()
