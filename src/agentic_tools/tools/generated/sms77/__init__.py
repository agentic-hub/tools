# sms77 toolkit
from langchain.tools import BaseTool
from typing import List

def get_sms77_tools() -> List[BaseTool]:
    """Get all sms77 tools."""
    from . import operations
    return operations.get_tools()

class SmsToolkit:
    """Toolkit for interacting with sms77."""

    def __init__(self):
        """Initialize the sms77 toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all sms77 tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all sms77 tools with default credentials."""
        return get_sms77_tools()
