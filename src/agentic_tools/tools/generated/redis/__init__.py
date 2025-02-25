# redis toolkit
from langchain.tools import BaseTool
from typing import List

def get_redis_tools() -> List[BaseTool]:
    """Get all redis tools."""
    from . import operations
    return operations.get_tools()

class RedisToolkit:
    """Toolkit for interacting with redis."""

    def __init__(self):
        """Initialize the redis toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all redis tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all redis tools with default credentials."""
        return get_redis_tools()
