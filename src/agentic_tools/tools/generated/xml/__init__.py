# xml toolkit
from langchain.tools import BaseTool
from typing import List

def get_xml_tools() -> List[BaseTool]:
    """Get all xml tools."""
    from . import operations
    return operations.get_tools()

class XmlToolkit:
    """Toolkit for interacting with xml."""

    def __init__(self):
        """Initialize the xml toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all xml tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all xml tools with default credentials."""
        return get_xml_tools()
