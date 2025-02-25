# urlscanio toolkit
from langchain.tools import BaseTool
from typing import List

def get_urlscanio_tools() -> List[BaseTool]:
    """Get all urlscanio tools."""
    from . import operations
    return operations.get_tools()

class UrlscanioToolkit:
    """Toolkit for interacting with urlscanio."""

    def __init__(self):
        """Initialize the urlscanio toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all urlscanio tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all urlscanio tools with default credentials."""
        return get_urlscanio_tools()
