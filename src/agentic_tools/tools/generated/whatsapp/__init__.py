# whatsapp toolkit
from langchain.tools import BaseTool
from typing import List

def get_whatsapp_tools() -> List[BaseTool]:
    """Get all whatsapp tools."""
    from . import operations
    return operations.get_tools()

class WhatsappToolkit:
    """Toolkit for interacting with whatsapp."""

    def __init__(self):
        """Initialize the whatsapp toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all whatsapp tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all whatsapp tools with default credentials."""
        return get_whatsapp_tools()
