# awss3 toolkit
from langchain.tools import BaseTool
from typing import List

def get_awss3_tools() -> List[BaseTool]:
    """Get all awss3 tools."""
    from . import operations
    return operations.get_tools()

class AwsS3Toolkit:
    """Toolkit for interacting with awss3."""

    def __init__(self):
        """Initialize the awss3 toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awss3 tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awss3 tools with default credentials."""
        return get_awss3_tools()
