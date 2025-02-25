# mqtt toolkit
from langchain.tools import BaseTool
from typing import List

def get_mqtt_tools() -> List[BaseTool]:
    """Get all mqtt tools."""
    from . import operations
    return operations.get_tools()

class MqttToolkit:
    """Toolkit for interacting with mqtt."""

    def __init__(self):
        """Initialize the mqtt toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mqtt tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mqtt tools with default credentials."""
        return get_mqtt_tools()
