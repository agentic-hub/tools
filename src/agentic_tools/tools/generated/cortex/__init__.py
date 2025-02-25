# cortex toolkit
from langchain.tools import BaseTool
from typing import List

def get_cortex_tools() -> List[BaseTool]:
    """Get all cortex tools."""
    from . import operations
    return operations.get_tools()

class CortexToolkit:
    """Toolkit for interacting with cortex."""

    def __init__(self):
        """Initialize the cortex toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all cortex tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all cortex tools with default credentials."""
        return get_cortex_tools()
