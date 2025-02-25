# mandrill toolkit
from langchain.tools import BaseTool
from typing import List

def get_mandrill_tools() -> List[BaseTool]:
    """Get all mandrill tools."""
    from . import operations
    return operations.get_tools()

class MandrillToolkit:
    """Toolkit for interacting with mandrill."""

    def __init__(self):
        """Initialize the mandrill toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all mandrill tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all mandrill tools with default credentials."""
        return get_mandrill_tools()
