# flow toolkit
from langchain.tools import BaseTool
from typing import List

def get_flow_tools() -> List[BaseTool]:
    """Get all flow tools."""
    from . import operations
    return operations.get_tools()

class FlowToolkit:
    """Toolkit for interacting with flow."""

    def __init__(self):
        """Initialize the flow toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all flow tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all flow tools with default credentials."""
        return get_flow_tools()
