# html toolkit
from langchain.tools import BaseTool
from typing import List

def get_html_tools() -> List[BaseTool]:
    """Get all html tools."""
    from . import operations
    return operations.get_tools()

class HtmlToolkit:
    """Toolkit for interacting with html."""

    def __init__(self):
        """Initialize the html toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all html tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all html tools with default credentials."""
        return get_html_tools()
