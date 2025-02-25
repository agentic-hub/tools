# invoiceninja toolkit
from langchain.tools import BaseTool
from typing import List

def get_invoiceninja_tools() -> List[BaseTool]:
    """Get all invoiceninja tools."""
    from . import operations
    return operations.get_tools()

class InvoiceninjaToolkit:
    """Toolkit for interacting with invoiceninja."""

    def __init__(self):
        """Initialize the invoiceninja toolkit."""

    def get_tools(self) -> List[BaseTool]:
        """Get all invoiceninja tools with the configured credentials."""
        from . import operations
        tools = operations.get_tools()
        return tools

    @staticmethod
    def get_default_tools() -> List[BaseTool]:
        """Get all invoiceninja tools with default credentials."""
        return get_invoiceninja_tools()
