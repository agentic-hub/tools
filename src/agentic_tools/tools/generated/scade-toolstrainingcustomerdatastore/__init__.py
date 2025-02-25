# scade-toolstrainingcustomerdatastore toolkit
from langchain.tools import BaseTool
from typing import List

def get_scade-toolstrainingcustomerdatastore_tools() -> List[BaseTool]:
    """Get all scade-toolstrainingcustomerdatastore tools."""
    from . import operations
    return operations.get_tools()

class ScadeToolstrainingcustomerdatastoreToolkit:
    """Toolkit for interacting with scade-toolstrainingcustomerdatastore."""

    def __init__(self):
        """Initialize the scade-toolstrainingcustomerdatastore toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all scade-toolstrainingcustomerdatastore tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all scade-toolstrainingcustomerdatastore tools with default credentials."""
        return get_scade-toolstrainingcustomerdatastore_tools()
