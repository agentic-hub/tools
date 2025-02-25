# uptimerobot toolkit
from langchain.tools import BaseTool
from typing import List

def get_uptimerobot_tools() -> List[BaseTool]:
    """Get all uptimerobot tools."""
    from . import operations
    return operations.get_tools()

class UptimerobotToolkit:
    """Toolkit for interacting with uptimerobot."""

    def __init__(self):
        """Initialize the uptimerobot toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all uptimerobot tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all uptimerobot tools with default credentials."""
        return get_uptimerobot_tools()
