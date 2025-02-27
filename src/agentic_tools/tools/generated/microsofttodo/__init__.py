# microsofttodo toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_microsofttodo_tools() -> List[BaseTool]:
    """Get all microsofttodo tools."""
    from . import operations
    return operations.get_tools()

class MicrosofttodoCredentials(BaseModel):
    """Credentials for microsofttodo authentication."""
    microsoft_to_do_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="microsoftToDoOAuth2Api")

class MicrosofttodoToolkit(AgenticHubToolkit):
    """Toolkit for interacting with microsofttodo."""

    def __init__(self, credentials: Optional[MicrosofttodoCredentials] = None):
        """Initialize the microsofttodo toolkit with optional credentials.

        Args:
            credentials: MicrosofttodoCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all microsofttodo tools with the configured credentials."""
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
        """Get all microsofttodo tools with default credentials."""
        return get_microsofttodo_tools()
