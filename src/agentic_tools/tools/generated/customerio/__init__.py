# customerio toolkit
from langchain.tools import BaseTool
from typing import List

def get_customerio_tools() -> List[BaseTool]:
    """Get all customerio tools."""
    from . import operations
    return operations.get_tools()

class CustomerioToolkit:
    """Toolkit for interacting with customerio."""

    def __init__(self):
        """Initialize the customerio toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all customerio tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all customerio tools with default credentials."""
        return get_customerio_tools()
