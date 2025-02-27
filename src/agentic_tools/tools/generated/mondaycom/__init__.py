# mondaycom toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_mondaycom_tools() -> List[BaseTool]:
    """Get all mondaycom tools."""
    from . import operations
    return operations.get_tools()

class MondaycomCredentials(BaseModel):
    """Credentials for mondaycom authentication."""
    monday_com_api: Optional[Dict[str, Any]] = Field(None, description="mondayComApi")
    monday_com_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="mondayComOAuth2Api")

class MondaycomToolkit(AgenticHubToolkit):
    """Toolkit for interacting with mondaycom."""

    def __init__(self, credentials: Optional[MondaycomCredentials] = None):
        """Initialize the mondaycom toolkit with optional credentials.

        Args:
            credentials: MondaycomCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all mondaycom tools with the configured credentials."""
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
        """Get all mondaycom tools with default credentials."""
        return get_mondaycom_tools()
