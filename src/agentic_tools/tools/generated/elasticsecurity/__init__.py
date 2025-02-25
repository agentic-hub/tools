# elasticsecurity toolkit
from langchain.tools import BaseTool
from typing import List

def get_elasticsecurity_tools() -> List[BaseTool]:
    """Get all elasticsecurity tools."""
    from . import operations
    return operations.get_tools()

class ElasticsecurityToolkit:
    """Toolkit for interacting with elasticsecurity."""

    def __init__(self):
        """Initialize the elasticsecurity toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all elasticsecurity tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all elasticsecurity tools with default credentials."""
        return get_elasticsecurity_tools()
