# invoiceNinja toolkit
from langchain.tools import BaseTool
from typing import List

def get_invoiceninja_tools() -> List[BaseTool]:
    """Get all invoiceNinja tools."""
    from . import operations
    return operations.get_tools()
