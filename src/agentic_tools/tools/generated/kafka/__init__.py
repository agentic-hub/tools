# kafka toolkit
from langchain.tools import BaseTool
from typing import List

def get_kafka_tools() -> List[BaseTool]:
    """Get all kafka tools."""
    from . import operations
    return operations.get_tools()

class KafkaToolkit:
    """Toolkit for interacting with kafka."""

    def __init__(self):
        """Initialize the kafka toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all kafka tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all kafka tools with default credentials."""
        return get_kafka_tools()
