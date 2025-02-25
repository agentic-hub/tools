# rabbitmq toolkit
from langchain.tools import BaseTool
from typing import List

def get_rabbitmq_tools() -> List[BaseTool]:
    """Get all rabbitmq tools."""
    from . import operations
    return operations.get_tools()

class RabbitmqToolkit:
    """Toolkit for interacting with rabbitmq."""

    def __init__(self):
        """Initialize the rabbitmq toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all rabbitmq tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all rabbitmq tools with default credentials."""
        return get_rabbitmq_tools()
