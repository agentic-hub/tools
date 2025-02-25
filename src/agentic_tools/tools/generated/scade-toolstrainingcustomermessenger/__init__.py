# scade-toolstrainingcustomermessenger toolkit
from langchain.tools import BaseTool
from typing import List

def get_scade-toolstrainingcustomermessenger_tools() -> List[BaseTool]:
    """Get all scade-toolstrainingcustomermessenger tools."""
    from . import operations
    return operations.get_tools()

class ScadeToolstrainingcustomermessengerToolkit:
    """Toolkit for interacting with scade-toolstrainingcustomermessenger."""

    def __init__(self):
        """Initialize the scade-toolstrainingcustomermessenger toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all scade-toolstrainingcustomermessenger tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all scade-toolstrainingcustomermessenger tools with default credentials."""
        return get_scade-toolstrainingcustomermessenger_tools()
