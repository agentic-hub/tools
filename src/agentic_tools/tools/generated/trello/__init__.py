# trello toolkit
from langchain.tools import BaseTool
from typing import List

def get_trello_tools() -> List[BaseTool]:
    """Get all trello tools."""
    from . import operations
    return operations.get_tools()

class TrelloToolkit:
    """Toolkit for interacting with trello."""

    def __init__(self):
        """Initialize the trello toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all trello tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all trello tools with default credentials."""
        return get_trello_tools()
