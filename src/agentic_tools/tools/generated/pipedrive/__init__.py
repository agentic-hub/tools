# pipedrive toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_pipedrive_tools() -> List[BaseTool]:
    """Get all pipedrive tools."""
    from . import operations
    return operations.get_tools()

class PipedriveCredentials(BaseModel):
    """Credentials for pipedrive authentication."""
    pipedrive_api: Optional[Dict[str, Any]] = Field(None, description="pipedriveApi")
    pipedrive_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="pipedriveOAuth2Api")

class PipedriveToolkit(AgenticHubToolkit):
    """Toolkit for interacting with pipedrive."""

    def __init__(self, credentials: Optional[PipedriveCredentials] = None):
        """Initialize the pipedrive toolkit with optional credentials.

        Args:
            credentials: PipedriveCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all pipedrive tools with the configured credentials."""
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
        """Get all pipedrive tools with default credentials."""
        return get_pipedrive_tools()
