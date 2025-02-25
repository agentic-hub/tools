# airtable toolkit
from langchain.tools import BaseTool
from typing import List

def get_airtable_tools() -> List[BaseTool]:
    """Get all airtable tools."""
    from . import operations
    return operations.get_tools()

class AirtableToolkit:
    """Toolkit for interacting with airtable."""

    def __init__(self):
        """Initialize the airtable toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all airtable tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all airtable tools with default credentials."""
        return get_airtable_tools()
