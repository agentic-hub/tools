# monicacrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_monicacrm_tools() -> List[BaseTool]:
    """Get all monicacrm tools."""
    from . import operations
    return operations.get_tools()

class MonicacrmToolkit:
    """Toolkit for interacting with monicacrm."""

    def __init__(self):
        """Initialize the monicacrm toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all monicacrm tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all monicacrm tools with default credentials."""
        return get_monicacrm_tools()
