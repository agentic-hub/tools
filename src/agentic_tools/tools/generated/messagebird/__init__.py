# messagebird toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_messagebird_tools() -> List[BaseTool]:
    """Get all messagebird tools."""
    from . import operations
    return operations.get_tools()

class MessagebirdCredentials(BaseModel):
    """Credentials for messagebird authentication."""
    message_bird_api: Optional[Dict[str, Any]] = Field(None, description="messageBirdApi")

class MessagebirdToolkit(AgenticHubToolkit):
    """Toolkit for interacting with messagebird."""

    def __init__(self, credentials: Optional[MessagebirdCredentials] = None):
        """Initialize the messagebird toolkit with optional credentials.

        Args:
            credentials: MessagebirdCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all messagebird tools with the configured credentials."""
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
        """Get all messagebird tools with default credentials."""
        return get_messagebird_tools()
