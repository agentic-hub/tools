# elasticsearch toolkit
from langchain.tools import BaseTool
from typing import List

def get_elasticsearch_tools() -> List[BaseTool]:
    """Get all elasticsearch tools."""
    from . import operations
    return operations.get_tools()

class ElasticsearchToolkit:
    """Toolkit for interacting with elasticsearch."""

    def __init__(self):
        """Initialize the elasticsearch toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all elasticsearch tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all elasticsearch tools with default credentials."""
        return get_elasticsearch_tools()
