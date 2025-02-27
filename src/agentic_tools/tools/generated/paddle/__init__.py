# paddle toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_paddle_tools() -> List[BaseTool]:
    """Get all paddle tools."""
    from . import operations
    return operations.get_tools()

class PaddleCredentials(BaseModel):
    """Credentials for paddle authentication."""
    paddle_api: Optional[Dict[str, Any]] = Field(None, description="paddleApi")

class PaddleToolkit(AgenticHubToolkit):
    """Toolkit for interacting with paddle."""

    def __init__(self, credentials: Optional[PaddleCredentials] = None):
        """Initialize the paddle toolkit with optional credentials.

        Args:
            credentials: PaddleCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all paddle tools with the configured credentials."""
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
        """Get all paddle tools with default credentials."""
        return get_paddle_tools()
