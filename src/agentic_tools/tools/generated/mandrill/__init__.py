# mandrill toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mandrill_tools() -> List[BaseTool]:
    """Get all mandrill tools."""
    from . import operations
    return operations.get_tools()

class MandrillCredentials(BaseModel):
    """Credentials for mandrill authentication."""
    mandrill_api: Optional[Dict[str, Any]] = Field(None, description="mandrillApi")

class MandrillToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mandrill."""

    def __init__(self, credentials: Optional[MandrillCredentials] = None):
        """Initialize the mandrill toolkit with optional credentials.

        Args:
            credentials: MandrillCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mandrill tools with the configured credentials."""
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
        """Get all mandrill tools with default credentials."""
        return get_mandrill_tools()
