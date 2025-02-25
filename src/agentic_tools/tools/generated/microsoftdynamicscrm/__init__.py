# microsoftdynamicscrm toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftdynamicscrm_tools() -> List[BaseTool]:
    """Get all microsoftdynamicscrm tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftdynamicscrmToolkit:
    """Toolkit for interacting with microsoftdynamicscrm."""

    def __init__(self):
        """Initialize the microsoftdynamicscrm toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftdynamicscrm tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all microsoftdynamicscrm tools with default credentials."""
        return get_microsoftdynamicscrm_tools()
