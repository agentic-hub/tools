# sms77 toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_sms77_tools() -> List[BaseTool]:
    """Get all sms77 tools."""
    from . import operations
    return operations.get_tools()

class Sms77Credentials(BaseModel):
    """Credentials for sms77 authentication."""
    sms77_api: Optional[Dict[str, Any]] = Field(None, description="sms77Api")

class SmsToolkit(AgenticHubToolkit):
    """Toolkit for interacting with sms77."""

    def __init__(self, credentials: Optional[Sms77Credentials] = None):
        """Initialize the sms77 toolkit with optional credentials.

        Args:
            credentials: Sms77Credentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all sms77 tools with the configured credentials."""
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
        """Get all sms77 tools with default credentials."""
        return get_sms77_tools()
