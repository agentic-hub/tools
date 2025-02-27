# sendgrid toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_sendgrid_tools() -> List[BaseTool]:
    """Get all sendgrid tools."""
    from . import operations
    return operations.get_tools()

class SendgridCredentials(BaseModel):
    """Credentials for sendgrid authentication."""
    send_grid_api: Optional[Dict[str, Any]] = Field(None, description="sendGridApi")

class SendgridToolkit(AgenticHubToolkit):
    """Toolkit for interacting with sendgrid."""

    def __init__(self, credentials: Optional[SendgridCredentials] = None):
        """Initialize the sendgrid toolkit with optional credentials.

        Args:
            credentials: SendgridCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all sendgrid tools with the configured credentials."""
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
        """Get all sendgrid tools with default credentials."""
        return get_sendgrid_tools()
