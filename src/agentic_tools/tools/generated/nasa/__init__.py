# nasa toolkit
from langchain.tools import BaseTool
from typing import List

def get_nasa_tools() -> List[BaseTool]:
    """Get all nasa tools."""
    from . import operations
    return operations.get_tools()

class NasaToolkit:
    """Toolkit for interacting with nasa."""

    def __init__(self):
        """Initialize the nasa toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all nasa tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all nasa tools with default credentials."""
        return get_nasa_tools()
