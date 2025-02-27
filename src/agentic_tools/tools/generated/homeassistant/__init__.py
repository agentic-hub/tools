# homeassistant toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_homeassistant_tools() -> List[BaseTool]:
    """Get all homeassistant tools."""
    from . import operations
    return operations.get_tools()

class HomeassistantCredentials(BaseModel):
    """Credentials for homeassistant authentication."""
    home_assistant_api: Optional[Dict[str, Any]] = Field(None, description="homeAssistantApi")

class HomeassistantToolkit(AgenticHubToolkit):
    """Toolkit for interacting with homeassistant."""

    def __init__(self, credentials: Optional[HomeassistantCredentials] = None):
        """Initialize the homeassistant toolkit with optional credentials.

        Args:
            credentials: HomeassistantCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all homeassistant tools with the configured credentials."""
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
        """Get all homeassistant tools with default credentials."""
        return get_homeassistant_tools()
