# sendy toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_sendy_tools() -> List[BaseTool]:
    """Get all sendy tools."""
    from . import operations
    return operations.get_tools()

class SendyCredentials(BaseModel):
    """Credentials for sendy authentication."""
    sendy_api: Optional[Dict[str, Any]] = Field(None, description="sendyApi")

class SendyToolkit(AgenticHubToolkit):
    """Toolkit for interacting with sendy."""

    def __init__(self, credentials: Optional[SendyCredentials] = None):
        """Initialize the sendy toolkit with optional credentials.

        Args:
            credentials: SendyCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all sendy tools with the configured credentials."""
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
        """Get all sendy tools with default credentials."""
        return get_sendy_tools()
