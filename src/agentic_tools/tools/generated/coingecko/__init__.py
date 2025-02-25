# coingecko toolkit
from langchain.tools import BaseTool
from typing import List

def get_coingecko_tools() -> List[BaseTool]:
    """Get all coingecko tools."""
    from . import operations
    return operations.get_tools()

class CoingeckoToolkit:
    """Toolkit for interacting with coingecko."""

    def __init__(self):
        """Initialize the coingecko toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all coingecko tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all coingecko tools with default credentials."""
        return get_coingecko_tools()
