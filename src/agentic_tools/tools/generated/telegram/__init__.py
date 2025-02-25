# telegram toolkit
from langchain.tools import BaseTool
from typing import List

def get_telegram_tools() -> List[BaseTool]:
    """Get all telegram tools."""
    from . import operations
    return operations.get_tools()

class TelegramToolkit:
    """Toolkit for interacting with telegram."""

    def __init__(self):
        """Initialize the telegram toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all telegram tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all telegram tools with default credentials."""
        return get_telegram_tools()
