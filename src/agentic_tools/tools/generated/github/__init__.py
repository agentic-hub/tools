# github toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_github_tools() -> List[BaseTool]:
    """Get all github tools."""
    from . import operations
    return operations.get_tools()

class GithubCredentials(BaseModel):
    """Credentials for github authentication."""
    github_api: Optional[Dict[str, Any]] = Field(None, description="githubApi")
    github_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="githubOAuth2Api")

class GithubToolkit(AgenticHubToolkit):
    """Toolkit for interacting with github."""

    def __init__(self, credentials: Optional[GithubCredentials] = None):
        """Initialize the github toolkit with optional credentials.

        Args:
            credentials: GithubCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all github tools with the configured credentials."""
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
        """Get all github tools with default credentials."""
        return get_github_tools()
