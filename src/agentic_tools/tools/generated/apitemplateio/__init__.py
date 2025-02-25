# apitemplateio toolkit
from langchain.tools import BaseTool
from typing import List

def get_apitemplateio_tools() -> List[BaseTool]:
    """Get all apitemplateio tools."""
    from . import operations
    return operations.get_tools()

class ApitemplateioToolkit:
    """Toolkit for interacting with apitemplateio."""

    def __init__(self):
        """Initialize the apitemplateio toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all apitemplateio tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all apitemplateio tools with default credentials."""
        return get_apitemplateio_tools()
