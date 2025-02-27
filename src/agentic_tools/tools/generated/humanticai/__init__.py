# humanticai toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_humanticai_tools() -> List[BaseTool]:
    """Get all humanticai tools."""
    from . import operations
    return operations.get_tools()

class HumanticaiCredentials(BaseModel):
    """Credentials for humanticai authentication."""
    humantic_ai_api: Optional[Dict[str, Any]] = Field(None, description="humanticAiApi")

class HumanticaiToolkit(AgenticHubToolkit):
    """Toolkit for interacting with humanticai."""

    def __init__(self, credentials: Optional[HumanticaiCredentials] = None):
        """Initialize the humanticai toolkit with optional credentials.

        Args:
            credentials: HumanticaiCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all humanticai tools with the configured credentials."""
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
        """Get all humanticai tools with default credentials."""
        return get_humanticai_tools()
