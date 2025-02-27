# openai toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_openai_tools() -> List[BaseTool]:
    """Get all openai tools."""
    from . import operations
    return operations.get_tools()

class OpenaiCredentials(BaseModel):
    """Credentials for openai authentication."""
    open_ai_api: Optional[Dict[str, Any]] = Field(None, description="openAiApi")

class OpenaiToolkit(AgenticHubToolkit):
    """Toolkit for interacting with openai."""

    def __init__(self, credentials: Optional[OpenaiCredentials] = None):
        """Initialize the openai toolkit with optional credentials.

        Args:
            credentials: OpenaiCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all openai tools with the configured credentials."""
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
        """Get all openai tools with default credentials."""
        return get_openai_tools()
