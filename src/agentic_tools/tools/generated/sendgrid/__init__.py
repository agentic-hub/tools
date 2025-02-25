# sendgrid toolkit
from langchain.tools import BaseTool
from typing import List

def get_sendgrid_tools() -> List[BaseTool]:
    """Get all sendgrid tools."""
    from . import operations
    return operations.get_tools()

class SendgridToolkit:
    """Toolkit for interacting with sendgrid."""

    def __init__(self):
        """Initialize the sendgrid toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all sendgrid tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all sendgrid tools with default credentials."""
        return get_sendgrid_tools()
