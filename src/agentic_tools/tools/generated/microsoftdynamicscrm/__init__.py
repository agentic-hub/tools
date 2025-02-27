# microsoftdynamicscrm toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_microsoftdynamicscrm_tools() -> List[BaseTool]:
    """Get all microsoftdynamicscrm tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftdynamicscrmCredentials(BaseModel):
    """Credentials for microsoftdynamicscrm authentication."""
    microsoft_dynamics_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftDynamicsOAuth2Api")

class MicrosoftdynamicscrmToolkit(AgenticHubToolkit):
    """Toolkit for interacting with microsoftdynamicscrm."""

    def __init__(self, credentials: Optional[MicrosoftdynamicscrmCredentials] = None):
        """Initialize the microsoftdynamicscrm toolkit with optional credentials.

        Args:
            credentials: MicrosoftdynamicscrmCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftdynamicscrm tools with the configured credentials."""
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
        """Get all microsoftdynamicscrm tools with default credentials."""
        return get_microsoftdynamicscrm_tools()
