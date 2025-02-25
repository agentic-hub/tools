# autopilot toolkit
from langchain.tools import BaseTool
from typing import List

def get_autopilot_tools() -> List[BaseTool]:
    """Get all autopilot tools."""
    from . import operations
    return operations.get_tools()

class AutopilotToolkit:
    """Toolkit for interacting with autopilot."""

    def __init__(self):
        """Initialize the autopilot toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all autopilot tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all autopilot tools with default credentials."""
        return get_autopilot_tools()
