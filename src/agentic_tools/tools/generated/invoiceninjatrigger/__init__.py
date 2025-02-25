# invoiceNinjaTrigger toolkit
from langchain.tools import BaseTool
from typing import List

def get_invoiceninjatrigger_tools() -> List[BaseTool]:
    """Get all invoiceNinjaTrigger tools."""
    from . import operations
    return operations.get_tools()
