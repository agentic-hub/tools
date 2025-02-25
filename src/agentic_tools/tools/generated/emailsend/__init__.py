# emailsend toolkit
from langchain.tools import BaseTool
from typing import List

def get_emailsend_tools() -> List[BaseTool]:
    """Get all emailsend tools."""
    from . import operations
    return operations.get_tools()

class EmailsendToolkit:
    """Toolkit for interacting with emailsend."""

    def __init__(self):
        """Initialize the emailsend toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all emailsend tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all emailsend tools with default credentials."""
        return get_emailsend_tools()
