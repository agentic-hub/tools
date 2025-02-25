# htmlextract toolkit
from langchain.tools import BaseTool
from typing import List

def get_htmlextract_tools() -> List[BaseTool]:
    """Get all htmlextract tools."""
    from . import operations
    return operations.get_tools()

class HtmlextractToolkit:
    """Toolkit for interacting with htmlextract."""

    def __init__(self):
        """Initialize the htmlextract toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all htmlextract tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all htmlextract tools with default credentials."""
        return get_htmlextract_tools()
