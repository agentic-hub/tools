# paypal toolkit
from langchain.tools import BaseTool
from typing import List

def get_paypal_tools() -> List[BaseTool]:
    """Get all paypal tools."""
    from . import operations
    return operations.get_tools()

class PaypalToolkit:
    """Toolkit for interacting with paypal."""

    def __init__(self):
        """Initialize the paypal toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all paypal tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all paypal tools with default credentials."""
        return get_paypal_tools()
