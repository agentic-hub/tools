# splunk toolkit
from langchain.tools import BaseTool
from typing import List

def get_splunk_tools() -> List[BaseTool]:
    """Get all splunk tools."""
    from . import operations
    return operations.get_tools()

class SplunkToolkit:
    """Toolkit for interacting with splunk."""

    def __init__(self):
        """Initialize the splunk toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all splunk tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all splunk tools with default credentials."""
        return get_splunk_tools()
