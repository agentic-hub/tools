# msg91 toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_msg91_tools() -> List[BaseTool]:
    """Get all msg91 tools."""
    from . import operations
    return operations.get_tools()

class Msg91Credentials(BaseModel):
    """Credentials for msg91 authentication."""
    msg91_api: Optional[Dict[str, Any]] = Field(None, description="msg91Api")

class MsgToolkit(AgenticHubToolkit):
    """Toolkit for interacting with msg91."""

    def __init__(self, credentials: Optional[Msg91Credentials] = None):
        """Initialize the msg91 toolkit with optional credentials.

        Args:
            credentials: Msg91Credentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all msg91 tools with the configured credentials."""
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
        """Get all msg91 tools with default credentials."""
        return get_msg91_tools()
