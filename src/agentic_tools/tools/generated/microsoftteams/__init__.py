# microsoftteams toolkit
from langchain.tools import BaseTool
from typing import List

def get_microsoftteams_tools() -> List[BaseTool]:
    """Get all microsoftteams tools."""
    from . import operations
    return operations.get_tools()

class MicrosoftteamsToolkit:
    """Toolkit for interacting with microsoftteams."""

    def __init__(self):
        """Initialize the microsoftteams toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all microsoftteams tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all microsoftteams tools with default credentials."""
        return get_microsoftteams_tools()
