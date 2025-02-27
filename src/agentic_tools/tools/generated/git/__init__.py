# git toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_git_tools() -> List[BaseTool]:
    """Get all git tools."""
    from . import operations
    return operations.get_tools()

class GitCredentials(BaseModel):
    """Credentials for git authentication."""
    git_password: Optional[Dict[str, Any]] = Field(None, description="gitPassword")

class GitToolkit(AgenticHubToolkit):
    """Toolkit for interacting with git."""

    def __init__(self, credentials: Optional[GitCredentials] = None):
        """Initialize the git toolkit with optional credentials.

        Args:
            credentials: GitCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all git tools with the configured credentials."""
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
        """Get all git tools with default credentials."""
        return get_git_tools()
