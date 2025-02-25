# stripe toolkit
from langchain.tools import BaseTool
from typing import List

def get_stripe_tools() -> List[BaseTool]:
    """Get all stripe tools."""
    from . import operations
    return operations.get_tools()

class StripeToolkit:
    """Toolkit for interacting with stripe."""

    def __init__(self):
        """Initialize the stripe toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all stripe tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all stripe tools with default credentials."""
        return get_stripe_tools()
