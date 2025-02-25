# segment toolkit
from langchain.tools import BaseTool
from typing import List

def get_segment_tools() -> List[BaseTool]:
    """Get all segment tools."""
    from . import operations
    return operations.get_tools()

class SegmentToolkit:
    """Toolkit for interacting with segment."""

    def __init__(self):
        """Initialize the segment toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all segment tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all segment tools with default credentials."""
        return get_segment_tools()
