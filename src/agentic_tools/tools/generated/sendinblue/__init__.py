# sendinblue toolkit
from langchain.tools import BaseTool
from typing import List

def get_sendinblue_tools() -> List[BaseTool]:
    """Get all sendinblue tools."""
    from . import operations
    return operations.get_tools()

class SendinblueToolkit:
    """Toolkit for interacting with sendinblue."""

    def __init__(self):
        """Initialize the sendinblue toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all sendinblue tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all sendinblue tools with default credentials."""
        return get_sendinblue_tools()
