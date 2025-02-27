# sendinblue toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_sendinblue_tools() -> List[BaseTool]:
    """Get all sendinblue tools."""
    from . import operations
    return operations.get_tools()

class SendinblueCredentials(BaseModel):
    """Credentials for sendinblue authentication."""
    send_in_blue_api: Optional[Dict[str, Any]] = Field(None, description="sendInBlueApi")

class SendinblueToolkit(AgenticHubToolkit):
    """Toolkit for interacting with sendinblue."""

    def __init__(self, credentials: Optional[SendinblueCredentials] = None):
        """Initialize the sendinblue toolkit with optional credentials.

        Args:
            credentials: SendinblueCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all sendinblue tools with the configured credentials."""
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
        """Get all sendinblue tools with default credentials."""
        return get_sendinblue_tools()
