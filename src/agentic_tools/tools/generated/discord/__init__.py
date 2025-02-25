# discord toolkit
from langchain.tools import BaseTool
from typing import List

def get_discord_tools() -> List[BaseTool]:
    """Get all discord tools."""
    from . import operations
    return operations.get_tools()

class DiscordToolkit:
    """Toolkit for interacting with discord."""

    def __init__(self):
        """Initialize the discord toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all discord tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all discord tools with default credentials."""
        return get_discord_tools()
