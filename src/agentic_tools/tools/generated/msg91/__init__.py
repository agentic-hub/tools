# msg91 toolkit
from langchain.tools import BaseTool
from typing import List

def get_msg91_tools() -> List[BaseTool]:
    """Get all msg91 tools."""
    from . import operations
    return operations.get_tools()

class MsgToolkit:
    """Toolkit for interacting with msg91."""

    def __init__(self):
        """Initialize the msg91 toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all msg91 tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all msg91 tools with default credentials."""
        return get_msg91_tools()
