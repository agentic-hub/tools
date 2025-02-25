# disqus toolkit
from langchain.tools import BaseTool
from typing import List

def get_disqus_tools() -> List[BaseTool]:
    """Get all disqus tools."""
    from . import operations
    return operations.get_tools()

class DisqusToolkit:
    """Toolkit for interacting with disqus."""

    def __init__(self):
        """Initialize the disqus toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all disqus tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all disqus tools with default credentials."""
        return get_disqus_tools()
