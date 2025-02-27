# twist toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_twist_tools() -> List[BaseTool]:
    """Get all twist tools."""
    from . import operations
    return operations.get_tools()

class TwistCredentials(BaseModel):
    """Credentials for twist authentication."""
    twist_o_auth2_api: Optional[Dict[str, Any]] = Field(None, description="twistOAuth2Api")

class TwistToolkit(AgenticHubToolkit):
    """Toolkit for interacting with twist."""

    def __init__(self, credentials: Optional[TwistCredentials] = None):
        """Initialize the twist toolkit with optional credentials.

        Args:
            credentials: TwistCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all twist tools with the configured credentials."""
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
        """Get all twist tools with default credentials."""
        return get_twist_tools()
