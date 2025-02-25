# securityscorecard toolkit
from langchain.tools import BaseTool
from typing import List

def get_securityscorecard_tools() -> List[BaseTool]:
    """Get all securityscorecard tools."""
    from . import operations
    return operations.get_tools()

class SecurityscorecardToolkit:
    """Toolkit for interacting with securityscorecard."""

    def __init__(self):
        """Initialize the securityscorecard toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all securityscorecard tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all securityscorecard tools with default credentials."""
        return get_securityscorecard_tools()
