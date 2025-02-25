# paddle toolkit
from langchain.tools import BaseTool
from typing import List

def get_paddle_tools() -> List[BaseTool]:
    """Get all paddle tools."""
    from . import operations
    return operations.get_tools()

class PaddleToolkit:
    """Toolkit for interacting with paddle."""

    def __init__(self):
        """Initialize the paddle toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all paddle tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all paddle tools with default credentials."""
        return get_paddle_tools()
