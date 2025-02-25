# amqp toolkit
from langchain.tools import BaseTool
from typing import List

def get_amqp_tools() -> List[BaseTool]:
    """Get all amqp tools."""
    from . import operations
    return operations.get_tools()

class AmqpToolkit:
    """Toolkit for interacting with amqp."""

    def __init__(self):
        """Initialize the amqp toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all amqp tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all amqp tools with default credentials."""
        return get_amqp_tools()
