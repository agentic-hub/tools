# questdb toolkit
from langchain.tools import BaseTool
from typing import List

def get_questdb_tools() -> List[BaseTool]:
    """Get all questdb tools."""
    from . import operations
    return operations.get_tools()

class QuestdbToolkit:
    """Toolkit for interacting with questdb."""

    def __init__(self):
        """Initialize the questdb toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all questdb tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all questdb tools with default credentials."""
        return get_questdb_tools()
