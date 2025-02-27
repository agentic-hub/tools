# telegram toolkit
from agentic_tools.tools import BaseTool, BaseModel, Field
from agentic_tools.toolkit import AgenticHubToolkit
from typing import List, Optional, Dict, Any

def get_telegram_tools() -> List[BaseTool]:
    """Get all telegram tools."""
    from . import operations
    return operations.get_tools()

class TelegramCredentials(BaseModel):
    """Credentials for telegram authentication."""
    telegram_api: Optional[Dict[str, Any]] = Field(None, description="telegramApi")

class TelegramToolkit(AgenticHubToolkit):
    """Toolkit for interacting with telegram."""

    def __init__(self, credentials: Optional[TelegramCredentials] = None):
        """Initialize the telegram toolkit with optional credentials.

        Args:
            credentials: TelegramCredentials object containing authentication credentials
        """
        self.credentials = credentials

    def get_tools(self) -> List[BaseTool]:
        """Get all telegram tools with the configured credentials."""
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
        """Get all telegram tools with default credentials."""
        return get_telegram_tools()
