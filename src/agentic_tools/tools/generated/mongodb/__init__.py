# mongodb toolkit
from langchain.tools import BaseTool
from typing import List

def get_mongodb_tools() -> List[BaseTool]:
    """Get all mongodb tools."""
    from . import operations
    return operations.get_tools()

class MongodbToolkit:
    """Toolkit for interacting with mongodb."""

    def __init__(self):
        """Initialize the mongodb toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mongodb tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mongodb tools with default credentials."""
        return get_mongodb_tools()
