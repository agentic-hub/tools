# ftp toolkit
from langchain.tools import BaseTool
from typing import List

def get_ftp_tools() -> List[BaseTool]:
    """Get all ftp tools."""
    from . import operations
    return operations.get_tools()

class FtpToolkit:
    """Toolkit for interacting with ftp."""

    def __init__(self):
        """Initialize the ftp toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all ftp tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all ftp tools with default credentials."""
        return get_ftp_tools()
