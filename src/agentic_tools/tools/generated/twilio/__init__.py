# twilio toolkit
from langchain.tools import BaseTool
from typing import List

def get_twilio_tools() -> List[BaseTool]:
    """Get all twilio tools."""
    from . import operations
    return operations.get_tools()

class TwilioToolkit:
    """Toolkit for interacting with twilio."""

    def __init__(self):
        """Initialize the twilio toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all twilio tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all twilio tools with default credentials."""
        return get_twilio_tools()
