# pipedrive toolkit
from langchain.tools import BaseTool
from typing import List

def get_pipedrive_tools() -> List[BaseTool]:
    """Get all pipedrive tools."""
    from . import operations
    return operations.get_tools()

class PipedriveToolkit:
    """Toolkit for interacting with pipedrive."""

    def __init__(self):
        """Initialize the pipedrive toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all pipedrive tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all pipedrive tools with default credentials."""
        return get_pipedrive_tools()
