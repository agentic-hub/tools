# graphql toolkit
from langchain.tools import BaseTool
from typing import List

def get_graphql_tools() -> List[BaseTool]:
    """Get all graphql tools."""
    from . import operations
    return operations.get_tools()

class GraphqlToolkit:
    """Toolkit for interacting with graphql."""

    def __init__(self):
        """Initialize the graphql toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all graphql tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all graphql tools with default credentials."""
        return get_graphql_tools()
