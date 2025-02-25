# automizy toolkit
from langchain.tools import BaseTool
from typing import List

def get_automizy_tools() -> List[BaseTool]:
    """Get all automizy tools."""
    from . import operations
    return operations.get_tools()

class AutomizyToolkit:
    """Toolkit for interacting with automizy."""

    def __init__(self):
        """Initialize the automizy toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all automizy tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all automizy tools with default credentials."""
        return get_automizy_tools()
