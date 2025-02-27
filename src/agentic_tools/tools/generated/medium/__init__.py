# medium toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_medium_tools() -> List[BaseTool]:
    """Get all medium tools."""
    from . import operations
    return operations.get_tools()

class MediumCredentials(BaseModel):
    """Credentials for medium authentication."""
    medium_api: Optional[Dict[str, Any]] = Field(None, description="mediumApi")
    medium_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="mediumOAuth2Api")

class MediumToolkit(AgenticHubToolkit):
    """Toolkit for interacting with medium."""

    def __init__(self, credentials: Optional[MediumCredentials] = None):
        """Initialize the medium toolkit with optional credentials.

        Args:
            credentials: MediumCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all medium tools with the configured credentials."""
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
        """Get all medium tools with default credentials."""
        return get_medium_tools()
