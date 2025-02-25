# s3 toolkit
from langchain.tools import BaseTool
from typing import List

def get_s3_tools() -> List[BaseTool]:
    """Get all s3 tools."""
    from . import operations
    return operations.get_tools()

class SToolkit:
    """Toolkit for interacting with s3."""

    def __init__(self):
        """Initialize the s3 toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all s3 tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all s3 tools with default credentials."""
        return get_s3_tools()
