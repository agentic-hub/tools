# emailsend toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_emailsend_tools() -> List[BaseTool]:
    """Get all emailsend tools."""
    from . import operations
    return operations.get_tools()

class EmailsendCredentials(BaseModel):
    """Credentials for emailsend authentication."""
    smtp: Optional[Dict[str, Any]] = Field(None, description="smtp")

class EmailsendToolkit(AgenticHubToolkit):
    """Toolkit for interacting with emailsend."""

    def __init__(self, credentials: Optional[EmailsendCredentials] = None):
        """Initialize the emailsend toolkit with optional credentials.

        Args:
            credentials: EmailsendCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all emailsend tools with the configured credentials."""
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
        """Get all emailsend tools with default credentials."""
        return get_emailsend_tools()
