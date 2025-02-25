# openai toolkit
from langchain.tools import BaseTool
from typing import List

def get_openai_tools() -> List[BaseTool]:
    """Get all openai tools."""
    from . import operations
    return operations.get_tools()

class OpenaiToolkit:
    """Toolkit for interacting with openai."""

    def __init__(self):
        """Initialize the openai toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all openai tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all openai tools with default credentials."""
        return get_openai_tools()
