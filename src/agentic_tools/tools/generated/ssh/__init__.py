# ssh toolkit
from langchain.tools import BaseTool
from typing import List

def get_ssh_tools() -> List[BaseTool]:
    """Get all ssh tools."""
    from . import operations
    return operations.get_tools()

class SshToolkit:
    """Toolkit for interacting with ssh."""

    def __init__(self):
        """Initialize the ssh toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all ssh tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all ssh tools with default credentials."""
        return get_ssh_tools()
