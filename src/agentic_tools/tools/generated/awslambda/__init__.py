# awslambda toolkit
from langchain.tools import BaseTool
from typing import List

def get_awslambda_tools() -> List[BaseTool]:
    """Get all awslambda tools."""
    from . import operations
    return operations.get_tools()

class AwsLambdaToolkit:
    """Toolkit for interacting with awslambda."""

    def __init__(self):
        """Initialize the awslambda toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awslambda tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awslambda tools with default credentials."""
        return get_awslambda_tools()
