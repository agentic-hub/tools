# ssh toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_ssh_tools() -> List[BaseTool]:
    """Get all ssh tools."""
    from . import operations
    return operations.get_tools()

class SshCredentials(BaseModel):
    """Credentials for ssh authentication."""
    ssh_password: Optional[Dict[str, Any]] = Field(None, description="sshPassword")
    ssh_private_key: Optional[Dict[str, Any]] = Field(None, description="sshPrivateKey")

class SshToolkit(AgenticHubToolkit):
    """Toolkit for interacting with ssh."""

    def __init__(self, credentials: Optional[SshCredentials] = None):
        """Initialize the ssh toolkit with optional credentials.

        Args:
            credentials: SshCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all ssh tools with the configured credentials."""
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
        """Get all ssh tools with default credentials."""
        return get_ssh_tools()
