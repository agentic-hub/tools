# matrix toolkit
from langchain.tools import BaseTool
from typing import List

def get_matrix_tools() -> List[BaseTool]:
    """Get all matrix tools."""
    from . import operations
    return operations.get_tools()

class MatrixToolkit:
    """Toolkit for interacting with matrix."""

    def __init__(self):
        """Initialize the matrix toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all matrix tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all matrix tools with default credentials."""
        return get_matrix_tools()
