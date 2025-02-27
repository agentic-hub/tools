# gitlab toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_gitlab_tools() -> List[BaseTool]:
    """Get all gitlab tools."""
    from . import operations
    return operations.get_tools()

class GitlabCredentials(BaseModel):
    """Credentials for gitlab authentication."""
    gitlab_api: Optional[Dict[str, Any]] = Field(None, description="gitlabApi")
    gitlab_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="gitlabOAuth2Api")

class GitlabToolkit(AgenticHubToolkit):
    """Toolkit for interacting with gitlab."""

    def __init__(self, credentials: Optional[GitlabCredentials] = None):
        """Initialize the gitlab toolkit with optional credentials.

        Args:
            credentials: GitlabCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all gitlab tools with the configured credentials."""
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
        """Get all gitlab tools with default credentials."""
        return get_gitlab_tools()
