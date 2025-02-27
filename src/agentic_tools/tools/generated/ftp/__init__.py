# ftp toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_ftp_tools() -> List[BaseTool]:
    """Get all ftp tools."""
    from . import operations
    return operations.get_tools()

class FtpCredentials(BaseModel):
    """Credentials for ftp authentication."""
    ftp: Optional[Dict[str, Any]] = Field(None, description="ftp")
    sftp: Optional[Dict[str, Any]] = Field(None, description="sftp")

class FtpToolkit(AgenticHubToolkit):
    """Toolkit for interacting with ftp."""

    def __init__(self, credentials: Optional[FtpCredentials] = None):
        """Initialize the ftp toolkit with optional credentials.

        Args:
            credentials: FtpCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all ftp tools with the configured credentials."""
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
        """Get all ftp tools with default credentials."""
        return get_ftp_tools()
