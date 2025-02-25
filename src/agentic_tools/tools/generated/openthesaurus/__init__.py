# openthesaurus toolkit
from langchain.tools import BaseTool
from typing import List

def get_openthesaurus_tools() -> List[BaseTool]:
    """Get all openthesaurus tools."""
    from . import operations
    return operations.get_tools()

class OpenthesaurusToolkit:
    """Toolkit for interacting with openthesaurus."""

    def __init__(self):
        """Initialize the openthesaurus toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all openthesaurus tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all openthesaurus tools with default credentials."""
        return get_openthesaurus_tools()
