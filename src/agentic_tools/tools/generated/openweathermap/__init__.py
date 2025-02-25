# openweathermap toolkit
from langchain.tools import BaseTool
from typing import List

def get_openweathermap_tools() -> List[BaseTool]:
    """Get all openweathermap tools."""
    from . import operations
    return operations.get_tools()

class OpenweathermapToolkit:
    """Toolkit for interacting with openweathermap."""

    def __init__(self):
        """Initialize the openweathermap toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all openweathermap tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all openweathermap tools with default credentials."""
        return get_openweathermap_tools()
