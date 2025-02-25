# citrixadc toolkit
from langchain.tools import BaseTool
from typing import List

def get_citrixadc_tools() -> List[BaseTool]:
    """Get all citrixadc tools."""
    from . import operations
    return operations.get_tools()

class CitrixadcToolkit:
    """Toolkit for interacting with citrixadc."""

    def __init__(self):
        """Initialize the citrixadc toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all citrixadc tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all citrixadc tools with default credentials."""
        return get_citrixadc_tools()
