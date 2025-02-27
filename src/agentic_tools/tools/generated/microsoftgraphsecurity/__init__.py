# microsoftgraphsecurity toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_microsoftgraphsecurity_tools() -> List[BaseTool]:
    """Get all microsoftgraphsecurity tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftgraphsecurityCredentials(BaseModel):
    """Credentials for microsoftgraphsecurity authentication."""
    microsoft_graph_security_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftGraphSecurityOAuth2Api")

class MicrosoftgraphsecurityToolkit(AgenticHubToolkit):
    """Toolkit for interacting with microsoftgraphsecurity."""

    def __init__(self, credentials: Optional[MicrosoftgraphsecurityCredentials] = None):
        """Initialize the microsoftgraphsecurity toolkit with optional credentials.

        Args:
            credentials: MicrosoftgraphsecurityCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftgraphsecurity tools with the configured credentials."""
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
        """Get all microsoftgraphsecurity tools with default credentials."""
        return get_microsoftgraphsecurity_tools()
