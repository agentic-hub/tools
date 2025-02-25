# microsoftsql toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftsql_tools() -> List[BaseTool]:
    """Get all microsoftsql tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftsqlToolkit:
    """Toolkit for interacting with microsoftsql."""

    def __init__(self):
        """Initialize the microsoftsql toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftsql tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all microsoftsql tools with default credentials."""
        return get_microsoftsql_tools()
