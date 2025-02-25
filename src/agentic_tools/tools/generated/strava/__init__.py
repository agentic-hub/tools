# strava toolkit
from langchain.tools import BaseTool
from typing import List

def get_strava_tools() -> List[BaseTool]:
    """Get all strava tools."""
    from . import operations
    return operations.get_tools()

class StravaToolkit:
    """Toolkit for interacting with strava."""

    def __init__(self):
        """Initialize the strava toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all strava tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all strava tools with default credentials."""
        return get_strava_tools()
