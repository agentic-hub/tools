# pagerduty toolkit
from langchain.tools import BaseTool
from typing import List

def get_pagerduty_tools() -> List[BaseTool]:
    """Get all pagerduty tools."""
    from . import operations
    return operations.get_tools()

class PagerdutyToolkit:
    """Toolkit for interacting with pagerduty."""

    def __init__(self):
        """Initialize the pagerduty toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all pagerduty tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all pagerduty tools with default credentials."""
        return get_pagerduty_tools()
