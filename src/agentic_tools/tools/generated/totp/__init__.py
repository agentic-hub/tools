# totp toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_totp_tools() -> List[BaseTool]:
    """Get all totp tools."""
    from . import operations
    return operations.get_tools()

class TotpCredentials(BaseModel):
    """Credentials for totp authentication."""
    totp_api: Optional[Dict[str, Any]] = Field(None, description="totpApi")

class TotpToolkit(AgenticHubToolkit):
    """Toolkit for interacting with totp."""

    def __init__(self, credentials: Optional[TotpCredentials] = None):
        """Initialize the totp toolkit with optional credentials.

        Args:
            credentials: TotpCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all totp tools with the configured credentials."""
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
        """Get all totp tools with default credentials."""
        return get_totp_tools()
