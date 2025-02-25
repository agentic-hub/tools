# microsofttodo toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsofttodo_tools() -> List[BaseTool]:
    """Get all microsofttodo tools."""
    from . import operations
    return operations.get_tools()

class MicrosofttodoToolkit:
    """Toolkit for interacting with microsofttodo."""

    def __init__(self):
        """Initialize the microsofttodo toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all microsofttodo tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all microsofttodo tools with default credentials."""
        return get_microsofttodo_tools()
