# awscomprehend toolkit
from langchain.tools import BaseTool
from typing import List

def get_awscomprehend_tools() -> List[BaseTool]:
    """Get all awscomprehend tools."""
    from . import operations
    return operations.get_tools()

class AwsComprehendToolkit:
    """Toolkit for interacting with awscomprehend."""

    def __init__(self):
        """Initialize the awscomprehend toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awscomprehend tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awscomprehend tools with default credentials."""
        return get_awscomprehend_tools()
