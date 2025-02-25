# taiga toolkit
from langchain.tools import BaseTool
from typing import List

def get_taiga_tools() -> List[BaseTool]:
    """Get all taiga tools."""
    from . import operations
    return operations.get_tools()

class TaigaToolkit:
    """Toolkit for interacting with taiga."""

    def __init__(self):
        """Initialize the taiga toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all taiga tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all taiga tools with default credentials."""
        return get_taiga_tools()
