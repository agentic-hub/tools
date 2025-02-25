# sentryio toolkit
from langchain.tools import BaseTool
from typing import List

def get_sentryio_tools() -> List[BaseTool]:
    """Get all sentryio tools."""
    from . import operations
    return operations.get_tools()

class SentryioToolkit:
    """Toolkit for interacting with sentryio."""

    def __init__(self):
        """Initialize the sentryio toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all sentryio tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all sentryio tools with default credentials."""
        return get_sentryio_tools()
