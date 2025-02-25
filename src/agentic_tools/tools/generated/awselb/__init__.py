# awselb toolkit
from langchain.tools import BaseTool
from typing import List

def get_awselb_tools() -> List[BaseTool]:
    """Get all awselb tools."""
    from . import operations
    return operations.get_tools()

class AwsElbToolkit:
    """Toolkit for interacting with awselb."""

    def __init__(self):
        """Initialize the awselb toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all awselb tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all awselb tools with default credentials."""
        return get_awselb_tools()
